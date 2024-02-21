from django.urls import path

from health.views import HealthViewSet

app_name = "health"

urlpatterns = [
    path("", HealthViewSet.as_view({"get": "list"}), name="health-list"),
]
