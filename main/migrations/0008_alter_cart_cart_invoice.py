# Generated by Django 5.0.6 on 2024-11-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cart_cart_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_invoice',
            field=models.IntegerField(),
        ),
    ]
