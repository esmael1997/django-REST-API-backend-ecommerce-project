from apps.accounts.models import Profile
from django.contrib.auth import authenticate

class ProfileService:
    @staticmethod
    def update_profile(profile: Profile, validated_data: dict) -> Profile:
        """
        Update user profile with validated data
        """
        for attr, value in validated_data.items():
            setattr(profile, attr, value)

        profile.save()
        return profile

    @staticmethod
    def change_password(user, old_password: str, new_password: str):
        if not user.check_password(old_password):
            raise ValueError("Old password is incorrect")

        user.set_password(new_password)
        user.save()

        return user
    