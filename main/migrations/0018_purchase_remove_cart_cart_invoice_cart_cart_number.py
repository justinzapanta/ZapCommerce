# Generated by Django 5.0.6 on 2024-11-19 05:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_rename_cart_totalprice_cart_cart_product_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('purchase_cart_number', models.IntegerField()),
                ('purchase_total_price', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cart_invoice',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_number',
            field=models.IntegerField(default=1),
        ),
    ]