from rest_framework import serializers
from .models import *


class ConsumerHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumerHistory
        fields = "__all__"
