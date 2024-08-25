from django.contrib import admin
from .models import Product


@admin.action(description="Mark selected as approved")
def make_approved(modeladmin, request, queryset):
    queryset.update(approved=True)


@admin.action(description="Mark selected as not approved")
def make_not_approved(modeladmin, request, queryset):
    queryset.update(approved=False)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "origin_country",
        "barcode",
        "category",
    )
    search_fields = ("name", "origin_country", "barcode", "category")
    actions = [make_approved, make_not_approved]


admin.site.register(Product, ProductAdmin)
