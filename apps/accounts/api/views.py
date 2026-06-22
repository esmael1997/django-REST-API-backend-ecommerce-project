from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.services.password_reset_service import create_password_reset
from apps.accounts.api.serializers import (
    PasswordResetRequestSerializer,
    RegisterSerializer,
    LoginSerializer,
)
from apps.accounts.services.auth_service import AuthService

User = get_user_model()

class PasswordResetRequestAPIView(APIView):

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]

        user = User.objects.filter(email=email).first()

       
        if user:
            create_password_reset(user)

        return Response({"message": "If this email exists, reset link has been sent."},status=status.HTTP_200_OK)
    
class PasswordResetConfirmAPIView(APIView):
    pass
    
class RegisterAPIView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = AuthService.register_user(
            email=serializer.validated_data["email"],
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        return Response(
            {
                "message": "User registered successfully.",
                "user_id": user.id,
            },
            status=status.HTTP_201_CREATED,
        )
        
class LoginAPIView(APIView):

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        tokens = AuthService.login_user(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        return Response(
            {
                "message": "Login successful.",
                "access": tokens["access"],
                "refresh": tokens["refresh"],
            },
            status=status.HTTP_200_OK,
        )
        

        
