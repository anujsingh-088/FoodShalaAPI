# Generated by Django 2.0.13 on 2020-03-22 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 0, 55, 50, 635492)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 0, 55, 50, 633495)),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 0, 55, 50, 633461)),
        ),
    ]
