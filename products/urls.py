from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r"products", ProductViewSet)
# router.register(r"products/indian", IndianProductViewSet, basename="indian_products")


urlpatterns = [
    path("", include(router.urls)),
]
