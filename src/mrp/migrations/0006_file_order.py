# Generated by Django 3.0.2 on 2020-02-12 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrp', '0005_item_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='order',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
