from django.contrib.auth.tokens import PasswordResetTokenGenerator
from  django.utils import timezone
from datetime import timedelta

class CustomPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def check_token_expiry(self, user):
        if not hasattr(user, "password_reset_sent_at"):
            return True
        
        expiry_time = user.password_reset_sent_at + timedelta(hours=24)
        return timezone.now() > expiry_time
    
token_generator = CustomPasswordResetTokenGenerator()