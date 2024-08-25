from rest_framework import serializers

from products.models import Product


class RelatedProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    origin_country = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ("approved", "related_product")

    def get_origin_country(self, obj):
        return obj.get_origin_country_display()

    def get_category(self, obj):
        return obj.get_category_display()


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    origin_country = serializers.SerializerMethodField()
    related_product = RelatedProductSerializer(many=True, required=False)

    class Meta:
        model = Product
        exclude = ("approved",)
        depth = 1

    def get_origin_country(self, obj):
        return obj.get_origin_country_display()

    def get_category(self, obj):
        return obj.get_category_display()
