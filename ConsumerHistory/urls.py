from django.urls import path

from ConsumerHistory.views import ConsumerHistoryViewSet

app_name = "ConsumerHistory"

urlpatterns = [
    path("", ConsumerHistoryViewSet.as_view({"get": "list"}), name="ConsumerHistory-list"),
]
