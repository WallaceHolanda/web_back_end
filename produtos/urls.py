from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexproduto, name='indexproduto'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('adicionar/addproduto/', views.addproduto, name='addproduto'),
]
