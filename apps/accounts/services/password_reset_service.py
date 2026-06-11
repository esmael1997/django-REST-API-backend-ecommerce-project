from config import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from accounts.utils.tokens import token_generator
from accounts.tasks.email_tasks import send_password_reset_email_task


User = get_user_model()


def create_password_reset(user):

    user.password_reset_sent_at = timezone.now()
    user.save(update_fields=["password_reset_sent_at"])

    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = token_generator.make_token(user)

    reset_link = f"{settings.FRONTEND_URL}/reset-password/{uidb64}/{token}/"

    send_password_reset_email_task.delay(user.email, reset_link)

    return reset_link