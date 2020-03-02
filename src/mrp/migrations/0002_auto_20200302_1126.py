# Generated by Django 3.0.3 on 2020-03-02 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mrp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mastfile',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mast_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemmasterfile',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_master_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemmaster',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inv_items', to='mrp.ItemMasterFile'),
        ),
        migrations.AddField(
            model_name='invitem',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inv_items', to='mrp.InvFile'),
        ),
        migrations.AddField(
            model_name='invfile',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bomitem',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bom_items', to='mrp.BomFile'),
        ),
        migrations.AddField(
            model_name='bomfile',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bom_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='period',
            unique_together={('file', 'part_number', 'order')},
        ),
    ]
