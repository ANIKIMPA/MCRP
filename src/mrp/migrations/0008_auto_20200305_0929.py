# Generated by Django 3.0.3 on 2020-03-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrp', '0007_auto_20200305_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmaster',
            name='lot_size',
            field=models.CharField(choices=[('LFL', 'LFL'), ('FP', 'FP'), ('FQ', 'FQ'), ('EOQ', 'EOQ')], default='LFL', max_length=5),
        ),
    ]
