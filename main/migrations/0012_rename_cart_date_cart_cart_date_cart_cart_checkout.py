# Generated by Django 5.0.6 on 2024-11-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_cart_cart_date_alter_cart_cart_invoice_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cart_Date',
            new_name='cart_date',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_checkout',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
