# Generated by Django 4.2 on 2023-11-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0011_remove_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notecategory',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]