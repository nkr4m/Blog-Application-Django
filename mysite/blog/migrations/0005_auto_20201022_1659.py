# Generated by Django 3.1.1 on 2020-10-22 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201021_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 11, 29, 40, 285172, tzinfo=utc)),
        ),
    ]
