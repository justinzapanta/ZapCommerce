# Generated by Django 5.0.6 on 2024-12-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_alter_user_info_user_profilepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_id_stripe',
            field=models.CharField(max_length=200, null=True),
        ),
    ]