from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexproduto, name='indexproduto'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('adicionar/addproduto/', views.addproduto, name='addproduto'),
    path('apagarproduto/<int:id>', views.apagarproduto, name='apagarproduto'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('editar/editarproduto/<int:id>', views.editarproduto, name='editarproduto'),
]
