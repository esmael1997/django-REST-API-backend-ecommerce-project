from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView
from .forms import LoginForm, RegisterForm
from django.core.cache import cache


class CustomPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset.html"
    email_template_name = "accounts/email/password_reset_email.html"
    success_url = "/password-reset/done/"

    def form_valid(self, form):

        email = form.cleaned_data["email"]

        # rate limit
        key = f"reset-{email}"
        if cache.get(key):
            messages.error(self.request, "Try again later")
            return redirect("password_reset")

        cache.set(key, True, timeout=60)

        return super().form_valid(form)
    
# ----------------------------
# Decorator: prevent logged-in users
# ----------------------------
def anonymous_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return view_func(request, *args, **kwargs)

    return wrapper


# ----------------------------
# LOGIN
# ----------------------------
def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm(request.POST or None)

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

                next_url = request.GET.get("next")
                return redirect(next_url or "home")

            messages.error(request, "Invalid credentials")

    return render(request, "apps/accounts/login.html", {"form": form})


# ----------------------------
# REGISTER
# ----------------------------
def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    form = RegisterForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "Account created successfully")

            return redirect("home")

    return render(request, "apps/accounts/register.html", {"form": form})


# ----------------------------
# LOGOUT
# ----------------------------
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect("login")


# ----------------------------
# CBV PAGES
# ----------------------------
class IndexView(TemplateView):
    template_name = "apps/accounts/index.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "apps/accounts/profile.html"