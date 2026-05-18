
'''
#from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_task(subject, body, to):

    send_mail(subject,body,settings.DEFAULT_FROM_EMAIL,to,fail_silently=False,backend="django.core.mail.backends.smtp.EmailBackend",)


@shared_task
def send_reset_email(subject, message, to_email):

    send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,[to_email],fail_silently=False,backend="django.core.mail.backends.smtp.EmailBackend",)
    
'''