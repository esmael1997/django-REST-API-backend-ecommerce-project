from apps.contact.models import ContactMessage


def create_contact_message(validated_data):
    return ContactMessage.objects.create(**validated_data)