# Generated by Django 3.0.10 on 2020-10-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0004_connect_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect',
            name='date',
            field=models.DateField(default='YYYY-MM-DD'),
        ),
    ]
