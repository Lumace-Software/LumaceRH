# Generated by Django 5.2 on 2025-04-18 17:07

import django.core.validators
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
            name='CategoriaIncidenciasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('codigo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Código')),
                ('efecto', models.CharField(choices=[('ADD', 'Percepción (suma)'), ('SUB', 'Deducción (resta)'), ('NONE', 'Sin efecto económico'), ('ACCUM', 'Acumulativa')], default='NONE', max_length=5, verbose_name='Efecto en nómina')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Categoría de Incidencias',
                'verbose_name_plural': 'Categorías de Incidencias',
                'db_table': 'incidencias_categoria',
            },
        ),
        migrations.CreateModel(
            name='TablaCalculosIncidenciasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('tipo_metodo', models.CharField(choices=[('FIXED', 'Monto fijo'), ('PERCENTAGE', 'Porcentaje del salario'), ('DAILY', 'Días de salario'), ('HOURLY', 'Horas (salario diario / horas jornada)'), ('POSITION_DIFF', 'Diferencia entre puestos'), ('CUSTOM', 'Fórmula personalizada')], max_length=20, verbose_name='Tipo de método')),
                ('monto_fijo', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Monto fijo')),
                ('porcentaje', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Porcentaje')),
                ('multiplicador', models.DecimalField(blank=True, decimal_places=2, help_text='Factor multiplicador (ej: 1.5 para un día y medio)', max_digits=5, null=True, verbose_name='Multiplicador')),
                ('work_hours_per_day', models.PositiveSmallIntegerField(default=8, help_text='Horas de jornada laboral para cálculo de hora extra', verbose_name='Horas por jornada')),
                ('formula', models.CharField(blank=True, help_text='Fórmula usando variables como {salary}, {days}, {hours}, etc.', max_length=500, null=True, verbose_name='Fórmula personalizada')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Método de cálculo',
                'verbose_name_plural': 'Métodos de cálculo',
                'db_table': 'metodos_calculo_incidencias',
            },
        ),
        migrations.CreateModel(
            name='TipoIncidenciaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('codigo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Código')),
                ('es_acumulable', models.BooleanField(default=False, help_text='Indica si esta incidencia se acumula hasta llegar a cierto número para generar un efecto', verbose_name='Es acumulativa')),
                ('conteo_acumulativo', models.PositiveSmallIntegerField(default=3, help_text='Número de incidencias que deben acumularse para generar el efecto', verbose_name='Conteo acumulativo')),
                ('periodo_reinicio', models.CharField(choices=[('NEVER', 'Nunca'), ('DAILY', 'Diario'), ('WEEKLY', 'Semanal'), ('BIWEEKLY', 'Quincenal'), ('MONTHLY', 'Mensual')], default='NEVER', help_text='Cuándo se reinicia el contador acumulativo', max_length=20, verbose_name='Período de reinicio')),
                ('max_dias', models.PositiveSmallIntegerField(default=0, help_text='Máximo de días permitidos (0 = sin límite)', verbose_name='Días máximos')),
                ('es_aprobada', models.BooleanField(default=True, verbose_name='Requiere aprobación')),
                ('requiere_documentacion', models.BooleanField(default=False, verbose_name='Requiere documentación')),
                ('afecta_asistencia', models.BooleanField(default=False, help_text='Indica si esta incidencia se considera una inasistencia', verbose_name='Afecta asistencia')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incident_types', to='incidencia.categoriaincidenciasmodel', verbose_name='Categoría')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('metodo_calculo', models.ForeignKey(blank=True, help_text='Método de cálculo para percepción/deducción. No aplicable para incidencias sin efecto económico.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='incident_types', to='incidencia.tablacalculosincidenciasmodel', verbose_name='Método de cálculo')),
                ('tipo_efecto_acumulativo', models.ForeignKey(blank=True, help_text='Tipo de incidencia que se genera al acumular el conteo especificado', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cumulative_sources', to='incidencia.tipoincidenciamodel', verbose_name='Incidencia resultante')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tipo de incidencia',
                'verbose_name_plural': 'Tipos de incidencias',
                'db_table': 'tipos_incidencias',
            },
        ),
    ]
