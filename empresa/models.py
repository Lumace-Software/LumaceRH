from django.db import models
from base.models import BaseModel
# Create your models here.

class EmpresaModel(BaseModel):
    razon_social = models.CharField(max_length=255, verbose_name='Razón Social', null=False, blank=False, help_text='Razón social de la empresa')
    nombre_comercial = models.CharField(max_length=255, verbose_name='Nombre Comercial', null=True, blank=True, help_text='Nombre comercial de la empresa')
    # Datos de Dirección
    calle = models.CharField(max_length=255, verbose_name='Calle', null=True, blank=True, help_text='Calle de la empresa')
    numero = models.CharField(max_length=10, verbose_name='Número', null=True, blank=True, help_text='Número de la calle de la empresa')
    ciudad = models.CharField(max_length=255, verbose_name='Ciudad', null=True, blank=True, help_text='Ciudad de la empresa')
    codigo_postal = models.CharField(max_length=10, verbose_name='Código Postal', null=True, blank=True, help_text='Código postal de la empresa')
    provincia = models.CharField(max_length=255, verbose_name='Provincia', null=True, blank=True, help_text='Provincia de la empresa')
    pais = models.CharField(max_length=255, verbose_name='País', null=True, blank=True, help_text='País de la empresa')
    @property
    def direccion(self):
        return f'{self.calle} #{self.numero}, {self.ciudad}, C.P. {self.codigo_postal}. {self.provincia}, {self.pais}'
    direccion.fget.short_description = 'Dirección'
    # Datos de Contacto
    telefono = models.CharField(max_length=20, verbose_name='Teléfono', null=True, blank=True, help_text='Teléfono de la empresa')
    fax = models.CharField(max_length=20, verbose_name='Fax', null=True, blank=True, help_text='Fax de la empresa')
    email = models.EmailField(max_length=255, verbose_name='Email', null=True, blank=True, help_text='Email de la empresa')
    web = models.URLField(max_length=255, verbose_name='Web', null=True, blank=True, help_text='Página web de la empresa')
    # Datos de Identificación Fiscal
    rfc = models.CharField(max_length=13, verbose_name='RFC', null=True, blank=True, help_text='RFC de la empresa')
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table = 'empresas'
    def __str__(self):
        return self.razon_social