# Generated by Django 5.0.6 on 2024-12-06 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_user_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_review',
            name='review_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user_info'),
        ),
    ]
