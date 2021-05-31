# Generated by Django 3.1.2 on 2021-05-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pedido_nombre_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='registroHabitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accesorios', models.CharField(choices=[('d', 'desayuno'), ('a', 'aseo')], default='d', max_length=10)),
                ('habitacion', models.CharField(choices=[('s', 'small'), ('b', 'big')], default='s', max_length=10)),
            ],
        ),
    ]
