# Generated by Django 4.2 on 2023-07-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_rename_balance_invoiceitems_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoiceitems',
            old_name='tax',
            new_name='tax_amount',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='balance',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='grand_total',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='note',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='tax',
        ),
        migrations.AddField(
            model_name='invoiceitems',
            name='tax_info',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoiceitems',
            name='total_after_discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')], default='pending', max_length=15),
        ),
    ]