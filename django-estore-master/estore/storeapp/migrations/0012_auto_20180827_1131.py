# Generated by Django 2.0.5 on 2018-08-27 06:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0011_userinfo'),
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
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(on_delete='CASCADE', related_name='userinfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', related_name='order', to='storeapp.UserInfo'),
        ),
    ]