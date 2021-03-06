from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexvendedor, name='indexvendedor'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('adicionar/addvendedor/', views.addvendedor, name='addvendedor'),
    path('apagarvendedor/<int:id>', views.apagarvendedor, name='apagarvendedor'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('editar/editarvendedor/<int:id>', views.editarvendedor, name='editarvendedor'),
]
