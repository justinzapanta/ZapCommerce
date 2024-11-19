# Generated by Django 5.0.6 on 2024-10-29 11:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_image', models.ImageField(upload_to='')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_type', models.CharField(max_length=80)),
                ('product_size', models.CharField(max_length=50)),
                ('product_details', models.TextField()),
                ('product_total_star', models.FloatField()),
                ('product_total_sale', models.IntegerField()),
            ],
        ),
    ]