# Generated by Django 3.0.2 on 2020-03-07 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrp', '0002_auto_20200306_1458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bomitem',
            options={'ordering': ['file', 'id'], 'verbose_name': 'BomItem', 'verbose_name_plural': 'BomItems'},
        ),
        migrations.AlterModelOptions(
            name='mastitem',
            options={'ordering': ['file', 'id'], 'verbose_name': 'MastItem', 'verbose_name_plural': 'MastItems'},
        ),
    ]