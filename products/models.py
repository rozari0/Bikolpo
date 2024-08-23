from django.db import models


class Product(models.Model):
    class CountryChoices(models.TextChoices):
        INDIA = "IN", "India"
        BANGLADESH = "BD", "Bangladesh"
        OTHERS = "OTHERS", "Others"

    name = models.CharField(max_length=255, help_text="Enter the name of the product.")
    origin_country = models.CharField(
        max_length=10,
        choices=CountryChoices.choices,
        default=CountryChoices.INDIA,
        help_text="Select the country where the product's company is based.",
    )
    related_product = models.ManyToManyField(
        "self",
        blank=True,
        help_text="Select a parent product if this is an alternative.",
    )
    barcode = models.CharField(
        max_length=20,
        help_text="Optional: Enter the barcode of the product.",
        null=True,
        blank=True,
    )
    details = models.TextField(
        help_text="Add extra details if you want ",
        null=True,
        blank=True,
    )
    approved = models.BooleanField(
        default=False, help_text="Admin only: Check if verified."
    )

    def __str__(self):
        return self.origin_country + " - " + self.name
