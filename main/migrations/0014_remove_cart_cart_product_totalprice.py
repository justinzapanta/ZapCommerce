# Generated by Django 5.0.6 on 2024-11-05 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_cart_cart_product_totalprice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_product_totalPrice',
        ),
    ]
