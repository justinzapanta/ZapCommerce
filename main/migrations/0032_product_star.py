# Generated by Django 5.0.6 on 2024-12-05 03:31

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_products_product_total_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_star',
            fields=[
                ('rate_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('five_start_total', models.IntegerField()),
                ('four_star_total', models.IntegerField()),
                ('three_star_total', models.IntegerField()),
                ('two_star_total', models.IntegerField()),
                ('one_star_total', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products')),
            ],
        ),
    ]
