# Generated by Django 3.0.2 on 2020-04-27 20:23

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mrp', '0002_auto_20200321_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled Report', max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('removed', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
                'ordering': ['-created_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ReportItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=12)),
                ('yield_percent', models.DecimalField(decimal_places=3, default=0, max_digits=4, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])),
                ('lead_time', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('order_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('parent', models.CharField(blank=True, max_length=12, null=True)),
                ('carrying_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('qty', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('lot_size', models.CharField(choices=[('LFL', 'LFL'), ('FP', 'FP'), ('FQ', 'FQ'), ('EOQ', 'EOQ')], default='LFL', max_length=5)),
                ('safe_stock', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('factor', models.CharField(blank=True, max_length=30, null=True)),
                ('on_hand', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('order', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('removed', models.BooleanField(default=False)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='mrp.Report')),
            ],
            options={
                'verbose_name': 'ReportItem',
                'verbose_name_plural': 'ReportItems',
                'ordering': ['report', 'order'],
            },
        ),
        migrations.CreateModel(
            name='ReportPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('gross_requirement', models.IntegerField(default=0)),
                ('receipt', models.IntegerField(default=0)),
                ('on_hand', models.IntegerField(default=0)),
                ('net_requirement', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periods', to='mrp.ReportItem')),
            ],
            options={
                'verbose_name': 'ReportPeriod',
                'verbose_name_plural': 'ReportPeriods',
                'ordering': ['item', 'period'],
            },
        ),
    ]
