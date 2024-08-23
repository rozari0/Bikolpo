from .models import Product
from .serializers import ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = ["approved", "origin_country"]
    search_fields = ["name"]
