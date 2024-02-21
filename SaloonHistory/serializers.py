from rest_framework import serializers
from .models import *


class SaloonHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SaloonHistory
        fields = "__all__"
