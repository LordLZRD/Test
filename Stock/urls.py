from django.urls import path

from Stock.views import StockViewSet

app_name = "Stock"

urlpatterns = [
    path("", StockViewSet.as_view({"get": "list"}), name="Stock-list"),
]
