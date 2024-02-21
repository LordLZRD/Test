from rest_framework import serializers
from .models import *


class SaloonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saloon
        fields = "__all__"







