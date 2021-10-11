# Generated by Django 2.0.5 on 2018-08-27 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0014_auto_20180827_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete='CASCADE', related_name='product', to='storeapp.Item')),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='price',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='product',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', related_name='order', to='storeapp.UserInfo'),
        ),
    ]