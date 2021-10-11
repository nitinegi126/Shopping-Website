# Generated by Django 2.0.5 on 2018-08-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0007_auto_20180824_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='brand-slug'),
        ),
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='cat-slug'),
        ),
    ]
