# Generated by Django 4.2 on 2023-06-05 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_doctor_calender_color_alter_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorleave',
            name='week_day',
        ),
    ]