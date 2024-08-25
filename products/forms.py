from django import forms

from .models import Product


class ProductSearchForm(forms.Form):
    name = forms.CharField(
        label="Product Name",
        max_length=255,
        help_text="Enter the name of the product you want to search for.",
    )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "origin_country", "barcode", "parent_product"]
        help_texts = {
            "barcode": "Enter the barcode (UPC/EAN) of the product. Leave blank if not applicable."
        }
