from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Username"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"form-control",
            "placeholdr":"Password"
        })
    )
    
class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password1',
            'password2',
        )
        