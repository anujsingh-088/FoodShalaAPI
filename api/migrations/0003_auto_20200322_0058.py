# Generated by Django 2.0.13 on 2020-03-22 00:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200322_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 0, 58, 28, 211629)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 0, 58, 28, 210557)),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 0, 58, 28, 210515)),
        ),
    ]