# Generated by Django 3.0.2 on 2020-03-10 21:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mrp', '0009_auto_20200308_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastitem',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 21, 57, 42, 219181, tzinfo=utc)),
        ),
    ]