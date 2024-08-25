from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = ["approved", "origin_country", "category"]
    search_fields = ["name", "barcode"]
