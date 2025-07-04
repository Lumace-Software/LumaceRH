from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

# Create your views here.

class ActualizacionesView(TemplateView):
    template_name = 'actualizacion1.6.html'

    def get(self, request, *args, **kwargs):
        # Si el usuario está autenticado, redirige a otra página
        if request.user.is_authenticated:
            return redirect('dashboard')

        # Si no está autenticado, muestra la plantilla normal
        return super().get(request, *args, **kwargs)

class NovedadesView(TemplateView):
    template_name = 'actualizacion1.6.html'

class NovedadesView2(TemplateView):
    template_name = 'actualizacion1.7.html'
