# Generated by Django 3.1.1 on 2020-10-22 19:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20201023_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 19, 32, 23, 601076, tzinfo=utc)),
        ),
    ]
