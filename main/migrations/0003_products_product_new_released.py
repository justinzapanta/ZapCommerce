# Generated by Django 5.0.6 on 2024-10-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_products_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_new_released',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
