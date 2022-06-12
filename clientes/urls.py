from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('adicionar/addcliente/', views.addcliente, name='addcliente'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('editar/editarcliente/<int:id>', views.editarcliente, name='editarcliente'),
]
