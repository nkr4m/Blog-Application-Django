# Generated by Django 3.1.1 on 2020-10-22 17:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201022_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 17, 48, 24, 924868, tzinfo=utc)),
        ),
    ]
