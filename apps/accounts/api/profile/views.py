from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.accounts.selectors import get_profile
from rest_framework.generics import RetrieveUpdateAPIView
from apps.accounts.api.profile.serializers import (
    ProfileSerializer,
    ProfileUpdateSerializer,
    ChangePasswordSerializer,
)
from apps.accounts.api.profile.services import ProfileService
from rest_framework import status


class ProfileAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_profile(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return ProfileUpdateSerializer
        return ProfileSerializer

    def partial_update(self, request, *args, **kwargs):
        profile = self.get_object()

        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_profile = ProfileService.update_profile(
            profile=profile,
            validated_data=serializer.validated_data
        )

        return self.get_response(updated_profile)
    

class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        ProfileService.change_password(
            user=user,
            old_password=serializer.validated_data["old_password"],
            new_password=serializer.validated_data["new_password"],
        )

        return Response(
            {"message": "Password changed successfully"},
            status=status.HTTP_200_OK
        )
