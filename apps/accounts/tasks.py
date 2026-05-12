from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_reset_email(subject, message, to_email):

    send_mail(
        subject,
        message,
        "noreply@example.com",
        [to_email],
        fail_silently=False,
    )