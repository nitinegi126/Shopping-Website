# Generated by Django 2.0.5 on 2018-08-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_auto_20180824_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=models.CharField(max_length=200), unique=True),
        ),
    ]
