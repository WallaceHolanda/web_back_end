from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexproduto, name='indexproduto'),
]
