# Generated by Django 5.2 on 2025-04-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0011_alter_contratomodel_frecuencia_pago_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratomodel',
            name='frecuencia_pago',
            field=models.CharField(choices=[('S', 'Semanal'), ('M', 'Mensual'), ('Q', 'Quincenal'), ('A', 'Anual'), ('D', 'Diario')], max_length=1),
        ),
        migrations.AlterField(
            model_name='contratomodel',
            name='tipo_contrato',
            field=models.CharField(choices=[('S', 'Servicio'), ('D', 'Definido'), ('P', 'Indefinido'), ('T', 'Temporal')], max_length=1),
        ),
    ]
