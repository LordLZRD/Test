from django.urls import path

from Offer.views import OfferViewSet

app_name = "Offer"

urlpatterns = [
    path("", OfferViewSet.as_view({"get": "list"}), name="Offer-list"),
]
