# Generated by Django 4.2 on 2024-01-13 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_user_referred_by_source'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DoctorLeave',
            new_name='Leaves',
        ),
    ]