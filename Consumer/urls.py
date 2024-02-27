from django.urls import path

from Consumer.views import ConsumerViewSet

app_name = "Consumer"

urlpatterns = [
    path("", ConsumerViewSet.as_view({"get": "list"}), name="Consumer-list"),
]
