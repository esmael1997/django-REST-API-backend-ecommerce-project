
'''
from django.core.mail.backends.smtp import EmailBackend

from .tasks import send_email_task


class CeleryEmailBackend(EmailBackend):

    def send_messages(self, email_messages):

        for message in email_messages:

            send_email_task.delay(message.subject,message.body,message.to,)

        return len(email_messages)
        
'''