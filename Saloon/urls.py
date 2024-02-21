from django.urls import path

from Saloon.views import SaloonViewSet

app_name = "Saloon"

urlpatterns = [
    path("", SaloonViewSet.as_view({"get": "list"}), name="Saloon-list"),
]
