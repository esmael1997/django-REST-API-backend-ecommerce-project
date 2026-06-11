from django.contrib.auth.tokens import PasswordResetTokenGenerator
from  django.utils import timezone
from datetime import timedelta

token_generator = PasswordResetTokenGenerator()

