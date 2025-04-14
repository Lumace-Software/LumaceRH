from django.urls import path
from .views import PostulanteListView, PostulanteWizardView,NuevoUsuarioView,EmpleadoListView, EmpleadoWizardView

urlpatterns = [
    path('', PostulanteListView.as_view(), name='postulante_list'),  # Listar postulantes
    path('create/', PostulanteWizardView.as_view(), name='postulante_create'),

    path('nuevo_usuario/', NuevoUsuarioView.as_view(), name='nuevo_usuario'),
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleado/create/', EmpleadoWizardView.as_view(), name='empleado_create'),
]
