from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from apps.accounts.utils.tokens import token_generator

User = get_user_model()


def confirm_password_reset(*, uidb64: str, token: str, new_password: str):
    try:
        user_id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        raise ValidationError("Invalid reset link.")

    if not token_generator.check_token(user, token):
        raise ValidationError("Invalid or expired reset token.")

    validate_password(new_password, user)

    user.set_password(new_password)
    user.password_reset_sent_at = None
    user.save(update_fields=["password", "password_reset_sent_at"])

    return user