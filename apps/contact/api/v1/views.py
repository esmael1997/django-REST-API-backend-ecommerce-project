from rest_framework import generics, status
from rest_framework.response import Response

from apps.contact.api.v1.serializers import ContactMessageSerializer
from apps.contact.services.contact_service import create_contact_message


class ContactMessageAPIView(generics.GenericAPIView):
    serializer_class = ContactMessageSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_contact_message(serializer.validated_data)

        return Response({"message": "Message sent successfully"},status=status.HTTP_201_CREATED)