# Generated by Django 3.0.10 on 2020-10-22 18:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20201023_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 18, 46, 20, 990475, tzinfo=utc)),
        ),
    ]
