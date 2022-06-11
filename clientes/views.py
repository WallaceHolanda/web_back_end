from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Clientes

def index(request):
    listaClientes = Clientes.objects.all().values()
    template = loader.get_template('index.html')
    context = {
     'listaClientes':listaClientes,
    }
    return HttpResponse(template.render(context, request))


def adicionar(request):
    template = loader.get_template('adicionar.html')
    return HttpResponse(template.render({}, request))
# Create your views here.
