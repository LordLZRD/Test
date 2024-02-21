from rest_framework import serializers
from .models import *


class AutoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoList
        fields = "__all__"
