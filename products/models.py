from django.db import models


class Product(models.Model):
    class CountryChoices(models.TextChoices):
        INDIA = "IN", "India"
        BANGLADESH = "BD", "Bangladesh"
        OTHERS = "OTHERS", "Others"

    class ProductCategories(models.TextChoices):
        DEFAULT = "DEFAULT", "Default"
        PACKAGED_FOOD = "PF", "Packaged Food"
        BEVERAGES = "BEV", "Beverages"
        COOKING_ESSENTIALS = "CE", "Cooking Essentials"
        BAKING_SUPPLIES = "BS", "Baking Supplies"
        DAIRY_PRODUCTS = "DP", "Dairy Products"
        MEAT_AND_SEAFOOD = "MS", "Meat and Seafood"
        FROZEN_FOODS = "FF", "Frozen Foods"
        PERSONAL_CARE = "PC", "Personal Care Products"
        SANITARY_PRODUCTS = "SP", "Sanitary Products"
        HOUSEHOLD_CLEANING = "HC", "Household Cleaning Supplies"
        HEALTH_AND_WELLNESS = "HW", "Health and Wellness"
        BABY_PRODUCTS = "BP", "Baby Products"
        PET_SUPPLIES = "PS", "Pet Supplies"
        INTERNATIONAL_FOODS = "IF", "International and Specialty Foods"

    name = models.CharField(max_length=255, help_text="Enter the name of the product.")
    origin_country = models.CharField(
        max_length=10,
        choices=CountryChoices.choices,
        default=CountryChoices.INDIA,
        help_text="Select the country where the product's company is based.",
    )
    category = models.CharField(
        max_length=10,
        choices=ProductCategories.choices,
        default=ProductCategories.DEFAULT,
        help_text="Select the category of the product.",
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
