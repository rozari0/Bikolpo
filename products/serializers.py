from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = ("approved",)
        depth = 1
