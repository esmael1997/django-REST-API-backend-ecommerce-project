
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()



class AuthService:
    
    @staticmethod
    def login_user(*, email, password):

        user = authenticate(username=email,password=password,)

        if user is None:
            raise ValueError("Invalid credentials.")

        refresh = RefreshToken.for_user(user)

        return {
            "user": user,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
        
        
    @staticmethod
    def logout(*, refresh_token: str) -> None:
        token = RefreshToken(refresh_token)
        token.blacklist()

    @staticmethod
    def generate_reset_token(user):
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        return uid, token

    @staticmethod
    def validate_reset_token(uidb64, token):
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if not default_token_generator.check_token(user, token):
            raise ValueError("Invalid token")

        return user

    @staticmethod
    def reset_password(user, new_password):
        validate_password(new_password, user)
        user.set_password(new_password)
        user.save()
        
    @staticmethod
    def register_user(
        *,
        email,
        username,
        password,
        full_name=None,
    ):

        user = User.objects.create_user(
        email=email,
        username=username,
        password=password,
    )

        return user
    
