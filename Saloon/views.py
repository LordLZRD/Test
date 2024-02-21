from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, viewsets, mixins
from .serializers import *
from .mixins import SaloonMixin


class SaloonViewSet(SaloonMixin):
    queryset = Saloon.objects.all()










