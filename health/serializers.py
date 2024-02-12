from rest_framework import serializers


class HealthSerializer(serializers.Serializer):
    status = serializers.CharField(default="OK")
    message = serializers.CharField(default="The application is running")
