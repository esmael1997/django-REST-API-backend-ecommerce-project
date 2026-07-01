from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.services.password_reset_service import create_password_reset
from apps.accounts.api.auth.serializers import (
    PasswordResetRequestSerializer,
    RegisterSerializer,
    LoginSerializer,
    LogoutSerializer,
    PasswordResetConfirmSerializer
)
from apps.accounts.services.auth_service import AuthService
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from apps.accounts.api.auth.serializers import CurrentUserSerializer


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

    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        confirm_password_reset(
            uidb64=serializer.validated_data["uid"],
            token=serializer.validated_data["token"],
            new_password=serializer.validated_data["new_password"],
        )

        return Response(
            {
                "message": "Password reset successfully."
            },
            status=status.HTTP_200_OK,
        )
    
class RegisterAPIView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

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

        serializer = LoginSerializer(data=request.data,)

        serializer.is_valid(raise_exception=True,)

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
        
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        AuthService.logout(refresh_token=serializer.validated_data["refresh"])

        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_200_OK
        )
        
class CurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        serializer = CurrentUserSerializer(request.user)
        
        return Response(serializer.data)
        

        
