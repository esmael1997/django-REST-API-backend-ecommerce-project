from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from accounts.utils.tokens import token_generator
from accounts.tasks.email_tasks import send_password_reset_email_task

User = get_user_model()


def create_password_reset(user):

    user.password_reset_sent_at = timezone.now()
    user.save(update_fields=["password_reset_sent_at"])

    uid = user.pk
    token = token_generator.make_token(user)

    reset_link = f"http://127.0.0.1:8000/api/v1/auth/reset/{uid}/{token}/"

    send_password_reset_email_task.delay(user.email, reset_link)

    return reset_link