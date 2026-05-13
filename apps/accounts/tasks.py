from django.core.mail.backends.smtp import EmailBackend
from .tasks import send_email_task
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


class CeleryEmailBackend(EmailBackend):

    def send_messages(self, email_messages):

        for message in email_messages:

            subject = message.subject
            body = message.body
            to = message.to

            send_email_task.delay(subject, body, to)

        return len(email_messages)
    



@shared_task
def send_reset_email(subject, message, to_email):

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        fail_silently=False,
    )