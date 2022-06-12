from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('vendedores/', include('vendedores.urls')),
    path('clientes/', include('clientes.urls')),
    path('admin/', admin.site.urls),
]
