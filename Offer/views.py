from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, viewsets, mixins
from .serializers import *

class OfferViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


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
