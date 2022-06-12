from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
from django.urls import reverse
from .models import Vendedores

def index(request):
  listaVendedores = Vendedores.objects.all().values()
  template = loader.get_template('indexVendedores.html')
  context = {
    'listaVendedores': listaVendedores,
  }
  return HttpResponse(template.render(context, request))

def adicionar(request):
  template = loader.get_template('adicionarVendedor.html')
  return HttpResponse(template.render({}, request))

def addvendedor(request):
  vend_nome = request.POST['nome']
  vend_documento = request.POST['documento']
  vend_endereco = request.POST['endereco']
  vend_telefone = request.POST['telefone']
  vend_banco = request.POST['banco']
  vend_conta = request.POST['conta']
  vend_email = request.POST['email']
  vend_senha = request.POST['senha']
  vendedor = Vendedores(nome=vend_nome, documento=vend_documento, endereco=vend_endereco, telefone=vend_telefone, banco=vend_banco, conta=vend_conta, email=vend_email, senha=vend_senha)
  vendedor.save()
  return HttpResponseRedirect(reverse('index'))
