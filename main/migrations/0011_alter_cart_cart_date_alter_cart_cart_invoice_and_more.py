# Generated by Django 5.0.6 on 2024-11-04 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_cart_cart_product_total_qt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_Date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_invoice',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_product_size',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_product_total_qt',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_totalPrice',
            field=models.IntegerField(null=True),
        ),
    ]