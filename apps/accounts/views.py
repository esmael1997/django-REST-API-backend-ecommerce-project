from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import Group
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import LoginForm, RegisterForm

from apps.accounts.services.auth_service import AuthService

User = get_user_model()


throttle_scope = "password_reset"


class PasswordResetRequestAPIView(APIView):

    def post(self, request):
        email = request.data.get("email")
        ip = request.META.get("REMOTE_ADDR")

        if not email:
            return Response({"error": "Email is required"}, status=400)

        # anti-spam rate limit
        cache_key = f"reset-{ip}-{email}"
        if cache.get(cache_key):
            return Response({"error": "Too many requests"}, status=429)

        cache.set(cache_key, True, timeout=60)

        users = User.objects.filter(email=email, is_active=True)

        for user in users:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            reset_link = f"http://localhost:3000/reset-password?uid={uid}&token={token}"

            # TODO: Celery task
            # send_reset_email.delay(user.email, reset_link)

        return Response({"message": "If user exists, email sent"}, status=200)
    
class PasswordResetConfirmAPIView(APIView):

    def post(self, request):
        uidb64 = request.data.get("uid")
        token = request.data.get("token")
        new_password = request.data.get("new_password")

        if not uidb64 or not token or not new_password:
            return Response({"error": "Missing fields"}, status=400)

        # decode uid
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception:
            return Response({"error": "Invalid UID"}, status=400)

        # validate token
        if not default_token_generator.check_token(user, token):
            return Response({"error": "Invalid or expired token"}, status=400)

        # password strength check
        try:
            validate_password(new_password, user)
        except Exception as e:
            return Response({"error": e.messages}, status=400)

        # set password
        user.set_password(new_password)
        user.save()

        return Response({"message": "Password reset successful"}, status=200)
    
class LoginAPIView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=400)

        login(request, user)

        return Response({"message": "Login successful"}, status=200)
    
class RegisterAPIView(APIView):

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not all([username, email ,password]):
            return Response({"error": "Missing fields"}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # assign role
        group, _ = Group.objects.get_or_create(name="customer")
        user.groups.add(group)

        return Response({"message": "User created"}, status=201)
    
class LogoutAPIView(APIView):

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out"}, status=200)
    