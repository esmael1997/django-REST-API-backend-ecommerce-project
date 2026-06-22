from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task
def send_password_reset_email_task(email, reset_link):
    
    send_mail(
        subject="Password Reset Request",
        message=f"Click the link to reset your password: {reset_link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )