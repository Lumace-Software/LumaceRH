# Generated by Django 5.2 on 2025-04-15 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0006_empleadomodel_sucursal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleadomodel',
            options={'managed': True, 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelTable(
            name='empleadomodel',
            table='empleados',
        ),
    ]
