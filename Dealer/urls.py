from django.urls import path

from Dealer.views import DealerViewSet

app_name = "Dealer"

urlpatterns = [
    path("", DealerViewSet.as_view({"get": "list"}), name="Dealer-list"),
]
