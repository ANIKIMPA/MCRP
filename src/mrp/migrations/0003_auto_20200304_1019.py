# Generated by Django 3.0.3 on 2020-03-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrp', '0002_auto_20200302_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemmaster',
            old_name='scrap_percent',
            new_name='yield_percent',
        ),
        migrations.AlterField(
            model_name='itemmaster',
            name='lot_size',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]