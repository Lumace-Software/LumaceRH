from django.apps import AppConfig


class IncidenciaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'incidencia'
    def ready(self):
        import incidencia.signal
