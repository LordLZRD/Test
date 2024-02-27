from django.urls import path

from SaloonHistory.views import SaloonHistoryViewSet

app_name = "SaloonHistory"

urlpatterns = [
    path("", SaloonHistoryViewSet.as_view({"get": "list"}), name="SaloonHistory-list"),
]
