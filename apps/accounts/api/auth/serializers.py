from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from apps.accounts.models import User 

User = get_user_model()

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
class PasswordResetConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True,min_length=8,)
    password_confirm = serializers.CharField(write_only=True,min_length=8,)

    def validate_email(self, value):

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")

        return value

    def validate(self, attrs):

        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        validate_password(attrs["password"])

        return attrs
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True,)
    refresh = serializers.CharField()
    

    def validate(self, attrs):
        user = authenticate(username=attrs["email"],password=attrs["password"],)
        
        if user is None:
            raise serializers.ValidationError("Invalid email or password.")
        
        attrs["user"] = user
        
        return attrs
    
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
    
class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            
        )
        


        