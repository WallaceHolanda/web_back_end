from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
from django.urls import reverse
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

def addcliente(request):
  cli_nome = request.POST['nome']
  cli_cpf = request.POST['cpf']
  cli_nascimento = request.POST['nascimento']
  cli_email = request.POST['email']
  cli_senha = request.POST['senha']
  cliente = Clientes(nome=cli_nome, cpf=cli_cpf, nascimento=cli_nascimento, email=cli_email, senha=cli_senha)
  cliente.save()
  return HttpResponseRedirect(reverse('index'))

def apagar(request, id):
  cliente = Clientes.objects.get(id=id)
  cliente.delete()
  return HttpResponseRedirect(reverse('index'))
