from rest_framework import generics, status
from rest_framework.response import Response

from apps.newsletter.api.v1.serializers import NewsletterSubscribeSerializer
from apps.newsletter.services.newsletter_service import subscribe_email


class NewsletterSubscribeAPIView(generics.GenericAPIView):
    serializer_class = NewsletterSubscribeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj, created = subscribe_email(serializer.validated_data["email"])

        return Response(
            {
                "message": "Subscribed successfully",
                "created": created
            },
            status=status.HTTP_201_CREATED
        )