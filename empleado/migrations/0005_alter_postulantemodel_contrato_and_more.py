# Generated by Django 5.2 on 2025-05-31 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0009_alter_contratomodel_tipo_contrato'),
        ('empleado', '0004_empleadomodel_fecha_contratacion'),
        ('puesto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulantemodel',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_contrato', to='contrato.contratomodel'),
        ),
        migrations.AlterField(
            model_name='postulantemodel',
            name='puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_puesto', to='puesto.puestomodel'),
        ),
    ]
