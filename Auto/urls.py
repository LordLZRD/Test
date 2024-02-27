from django.urls import path

from Auto.views import AutoViewSet

app_name = "Auto"

urlpatterns = [
    path("", AutoViewSet.as_view({"get": "list"}), name="Auto-list"),
]
