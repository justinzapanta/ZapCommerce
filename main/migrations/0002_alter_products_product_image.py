# Generated by Django 5.0.6 on 2024-10-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default=None, null=True, upload_to='./main/static/img/project_img'),
        ),
    ]
