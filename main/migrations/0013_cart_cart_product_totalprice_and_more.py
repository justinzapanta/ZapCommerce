# Generated by Django 5.0.6 on 2024-11-05 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_cart_date_cart_cart_date_cart_cart_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_product_totalPrice',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_checkout',
            field=models.BooleanField(default=False),
        ),
    ]
