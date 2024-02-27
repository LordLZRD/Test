from .models import Saloon
from .serializers import *
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from WSDjango.default_mixin import GetPermissionsMixin, GetSerializerMixin


class SaloonMixin(
    GetSerializerMixin,
    # GetPermissionsMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet,
):

    serializer_classes = {
        "list": SaloonSerializer,
    }

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if "balance" in request.data:
            return Response({'error': 'Balance cannot be updated.'}, status=400)

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        if "balance" in request.data:
            return Response({'error': 'Balance cannot be updated.'}, status=400)

        return super().partial_update(request, *args, **kwargs)