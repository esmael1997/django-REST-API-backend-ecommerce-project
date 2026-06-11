from rest_framework import serializers
from apps.newsletter.models import NewsletterSubscriber


class NewsletterSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]