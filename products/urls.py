from django.urls import include, path
from rest_framework import routers

from .views import ProductViewSet

router = routers.DefaultRouter()

router.register(r"products", ProductViewSet)
# router.register(r"products/indian", IndianProductViewSet, basename="indian_products")


urlpatterns = [
    path("", include(router.urls)),
]
