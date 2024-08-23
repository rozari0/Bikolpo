# Generated by Django 5.1 on 2024-08-23 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_local',
        ),
        migrations.AddField(
            model_name='product',
            name='origin_country',
            field=models.CharField(choices=[('IN', 'India'), ('BD', 'Bangladesh'), ('OTHERS', 'Others')], default='IN', help_text="Select the country where the product's company is based.", max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Enter the name of the product.', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='parent_product',
            field=models.ForeignKey(blank=True, help_text='Select a parent product if this is an alternative.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alternatives', to='products.product'),
        ),
    ]
