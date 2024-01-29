from rest_framework import viewsets
from rest_framework.response import Response

from health.serializers import HealthSerializer


class HealthViewSet(viewsets.ViewSet):
    serializer_class = HealthSerializer

    def list(self, request):
        data = {"status": "OK", "message": "The application is running"}
        serializer = HealthSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.data)
