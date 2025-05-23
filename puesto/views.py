# Django
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
# Vistas
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# Modelos
from .models import PuestoModel
from django.db.models import ProtectedError
# Formularios
from .forms import PuestoForm
# Mixins
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

class PuestoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'puesto.view_puestomodel'
    model = PuestoModel
    template_name = 'puestos.html'
    context_object_name = 'puestos'
    paginate_by = 10
    ordering = ['nombre', 'created_at']

class PuestoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'puesto.add_puestomodel'    
    model = PuestoModel
    form_class = PuestoForm
    template_name = 'puesto_form.html'
    success_url = reverse_lazy('puesto_list')
    def form_valid(self, form):
        # Asignar el usuario antes de guardar
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

class PuestoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'puesto.view_puestomodel'
    model = PuestoModel
    template_name = 'puesto_detail.html'
    context_object_name = 'puesto'

class PuestoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'puesto.delete_puestomodel'
    model = PuestoModel
    context_object_name = 'puesto'
    template_name = 'puesto_confirm_delete.html'
    success_url = reverse_lazy('puesto_list')

    def post(self, request, *args, **kwargs):
        puesto = self.get_object()
        try:
            puesto.delete()
            messages.success(request, "Puesto eliminado correctamente.")
        except ProtectedError:
            messages.error(request, "No se puede eliminar el puesto porque está relacionado con otros registros.")
        return redirect(self.success_url)