from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.api.serializers import PasswordResetRequestSerializer
from accounts.services.password_reset_service import create_password_reset

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