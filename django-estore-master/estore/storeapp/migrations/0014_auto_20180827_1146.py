# Generated by Django 2.0.5 on 2018-08-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0013_auto_20180827_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='product',
            field=models.ForeignKey(blank=True, on_delete='CASCADE', related_name='product', to='storeapp.Item'),
        ),
    ]
