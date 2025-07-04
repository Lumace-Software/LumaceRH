from django.urls import path, include
from .views import EstadoIncidenciaUpdateView, IncidenciasGeneralListView, IncidenciasSucursalListView, IncidenciaUpdateView, EstadoIncdenciasGeneralUpdateView, IncidencasEmpleadoView, RetardoIncidenciaView, FaltaIncidenciaView
urlpatterns = [
    path('actualizar/<int:pk>/', EstadoIncidenciaUpdateView.as_view(), name='estado-incidencia-update'),
    path('', IncidenciasGeneralListView.as_view(), name='incidencias-general-list'),
    path('incidencias/sucursal/<int:pk>/', IncidenciasSucursalListView.as_view(), name='incidencias-sucursal-list'),
    path('incidencia/editar/<int:pk>/', IncidenciaUpdateView.as_view(), name='incidencia-update'),
    path('incidencias/editar/', EstadoIncdenciasGeneralUpdateView.as_view(), name='incidencias-general-update'),
    path('empleado/<int:pk>/', IncidencasEmpleadoView.as_view(), name='incidencias-empleado-view'),
    path('retardo/<int:pk>/', RetardoIncidenciaView.as_view(), name='retardo-incidencia-view'),
    path('falta/<int:pk>/', FaltaIncidenciaView.as_view(), name='falta-incidencia-view'),
]