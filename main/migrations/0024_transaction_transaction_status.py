# Generated by Django 5.0.6 on 2024-11-20 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_transaction_transaction_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_status',
            field=models.CharField(default='Paid', max_length=100),
        ),
    ]