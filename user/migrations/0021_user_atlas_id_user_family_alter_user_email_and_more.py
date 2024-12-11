# Generated by Django 4.2 on 2023-12-21 19:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='atlas_id',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='family',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9999999999'.", regex='^[\\+\\d{10,18}]?(?:[\\d\\-.\\s()]{10,20})$')]),
        ),
    ]