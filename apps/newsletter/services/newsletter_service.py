from apps.newsletter.models import NewsletterSubscriber


def subscribe_email(email: str):
    obj, created = NewsletterSubscriber.objects.get_or_create(
        email=email,
        defaults={"is_active": True}
    )
    return obj, created