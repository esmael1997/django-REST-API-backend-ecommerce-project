from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.contrib.auth.views import PasswordResetView
from django.core.cache import cache
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from functools import wraps
from django.contrib.auth.models import Group
from .forms import LoginForm, RegisterForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

from .tasks import send_reset_email


class CustomPasswordResetView(PasswordResetView):

    template_name = "accounts/password_reset.html"
    email_template_name = "accounts/email/password_reset_email.html"
    success_url = "/password-reset/done/"

    def form_valid(self, form):

        user_email = form.cleaned_data["email"]
        ip = self.request.META.get("REMOTE_ADDR")

        # rate limit (anti spam)
        cache_key = f"reset-{ip}-{user_email}"

        if cache.get(cache_key):
            messages.error(self.request, "Too many requests. Try later.")
            return redirect("password_reset")

        cache.set(cache_key, True, timeout=60)

        # user queryset (safe)
        from django.contrib.auth import get_user_model
        User = get_user_model()

        users = User.objects.filter(email=user_email, is_active=True)

        for user in users:

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            reset_link = f"http://localhost:8000/reset/{uid}/{token}/"

            subject = "Password Reset Request"

            message = f"""
Hello {user.username},

Click below link to reset your password:

{reset_link}

This link is valid for 48 hours.
"""

            # async email via celery
            send_reset_email.delay(subject, message, user_email)

        return super().form_valid(form)
    

# Decorator: prevent logged-in users

def anonymous_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect("home")

        return view_func(request, *args, **kwargs)

    return wrapper


# LOGIN

def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm(request.POST or None)

    next_url = request.POST.get("next") or request.GET.get("next")

    if request.method == "POST":

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)
                messages.success(request, "Login successful")

                if next_url and url_has_allowed_host_and_scheme(
                    next_url,
                    allowed_hosts={request.get_host()},
                    require_https=request.is_secure(),
                ):
                    return redirect(next_url)

                return redirect("home")

            messages.error(request, "Invalid credentials")

    return render(request, "apps/accounts/login.html", {
        "form": form,
        "next": next_url
    })
    
    


# REGISTER

def register_view(request):

    form = RegisterForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            user = form.save()

            # assign default role
            group = Group.objects.get(name="customer")
            user.groups.add(group)

            login(request, user)

            return redirect("home")
        
def is_admin(user):
    return user.groups.filter(name="admin").exists()


# LOGOUT

@require_POST
def logout_view(request):

    logout(request)
    messages.success(request, "You have been logged out successfully")

    return redirect("login")


def password_reset_confirm(request, uidb64, token):

    User = get_user_model()

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

    except:
        user = None

    if user is None or not default_token_generator.check_token(user, token):
        return render(request, "accounts/password_reset_invalid.html")

    if request.method == "POST":

        form = SetPasswordForm(user, request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = SetPasswordForm(user)

    return render(request, "accounts/password_reset_confirm.html", {
        "form": form
    })



# CBV PAGES

class IndexView(TemplateView):
    template_name = "apps/accounts/index.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "apps/accounts/profile.html"
    login_url = "login"