# Generated by Django 5.0.6 on 2024-12-07 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_user_info_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_info',
            old_name='user_role',
            new_name='user_roles',
        ),
    ]
