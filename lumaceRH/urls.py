"""
URL configuration for lumaceRH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("unicorn/", include("django_unicorn.urls")),
    path('tinymce/', include('tinymce.urls')),
    # allauth
    path('accounts/', include('allauth.urls')),
    # Rest Framework
    path('api-auth/', include('rest_framework.urls')),
    # Local apps
    path('', include('base.urls')),
    path('empresa/', include('empresa.urls')),
    path('sucursal/', include('sucursal.urls')),
    path('departamento/', include('departamento.urls')),
    path('puesto/', include('puesto.urls')),
    path('contrato/', include('contrato.urls')),
    path('personal/', include('empleado.urls')),
    path('incidencias/', include('incidencia.urls')),
]
