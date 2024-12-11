# Generated by Django 4.2 on 2023-06-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_doctortiming_week_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('', 'Select'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('', 'Select'), ('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')], default='', null=True),
        ),
    ]