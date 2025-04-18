# Generated by Django 5.2 on 2025-04-08 18:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContratoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tipo_contrato', models.CharField(choices=[('P', 'Indefinido'), ('T', 'Temporal'), ('D', 'Definido'), ('S', 'Servicio')], max_length=1)),
                ('horas_trabajo', models.IntegerField()),
                ('salario_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('frecuencia_pago', models.CharField(choices=[('B', 'Quincenal'), ('M', 'Mensual'), ('D', 'Diario'), ('A', 'Anual'), ('S', 'Semanal')], max_length=1)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
