# Generated by Django 5.0.6 on 2024-11-28 21:09

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_remove_cart_cart_date_transaction_transaction_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user_firstName', models.CharField(max_length=50)),
                ('user_lastName', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=250)),
                ('user_profilePicture', models.ImageField(default=None, null=True, upload_to='.main/static/image')),
                ('user_auth_credentials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]