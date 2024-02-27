from django.urls import path

from AutoList.views import AutoListViewSet

app_name = "AutoList"

urlpatterns = [
    path("", AutoListViewSet.as_view({"get": "list"}), name="AutoList-list"),
]
