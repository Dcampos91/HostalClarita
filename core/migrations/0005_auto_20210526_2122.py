# Generated by Django 3.2 on 2021-05-27 01:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_tipo_cama_tipohabitacion_tipo_hab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipohabitacion',
            name='datelle_habitacion',
        ),
        migrations.AddField(
            model_name='tipohabitacion',
            name='detalle_habitacion',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
