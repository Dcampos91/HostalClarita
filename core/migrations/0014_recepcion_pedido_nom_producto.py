# Generated by Django 3.2 on 2021-07-15 17:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_recepcion_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcion_pedido',
            name='nom_producto',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]