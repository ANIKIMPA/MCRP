# Generated by Django 3.0.2 on 2020-03-08 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrp', '0006_auto_20200308_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='bomfile',
            name='removed',
            field=models.BooleanField(default=0),
        ),
    ]