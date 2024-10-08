# Generated by Django 5.1 on 2024-08-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_product_barcode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="parent_product",
        ),
        migrations.AddField(
            model_name="product",
            name="foriegn_product",
            field=models.ManyToManyField(
                blank=True,
                help_text="Select a parent product if this is an alternative.",
                null=True,
                related_name="alternatives",
                to="products.product",
            ),
        ),
    ]
