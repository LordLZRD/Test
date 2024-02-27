from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from health.views import HealthViewSet
from Saloon.views import SaloonViewSet
from Auto.views import AutoViewSet
from AutoList.views import AutoListViewSet
from Consumer.views import ConsumerViewSet
from ConsumerHistory.views import ConsumerHistoryViewSet
from Dealer.views import DealerViewSet
from Offer.views import OfferViewSet
from SaloonHistory.views import SaloonHistoryViewSet
from Stock.views import StockViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="API Documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r"health", HealthViewSet, basename="health")
router.register(r"Saloon", SaloonViewSet, basename="Saloon")
router.register(r"Auto", AutoViewSet, basename="Auto")
router.register(r"AutoList", AutoListViewSet, basename="AutoList")
router.register(r"Consumer", ConsumerViewSet, basename="Consumer")
router.register(r"ConsumerHistory", ConsumerHistoryViewSet, basename="ConsumerHistory")
router.register(r"Dealer", DealerViewSet, basename="Dealer")
router.register(r"Offer", OfferViewSet, basename="Offer")
router.register(r"SaloonHistory", SaloonHistoryViewSet, basename="SaloonHistory")
router.register(r"Stock", StockViewSet, basename="Stock")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "swagger<str:format>",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
