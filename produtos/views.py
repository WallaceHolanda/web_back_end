from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
from django.urls import reverse
from .models import Produtos

def indexproduto(request):
  listaProdutos = Produtos.objects.all().values()
  template = loader.get_template('indexProdutos.html')
  context = {
    'listaProdutos': listaProdutos,
  }
  return HttpResponse(template.render(context, request))

def adicionar(request):
  template = loader.get_template('adicionarProduto.html')
  return HttpResponse(template.render({}, request))

def addproduto(request):
  prod_nome = request.POST['nome']
  prod_vendedor = request.POST['vendedor']
  prod_valor = request.POST['valor']
  prod_imagem = request.POST['imagem']

  produto = Produtos(nome=prod_nome, valor=prod_valor, imagem=prod_imagem, vendedor=prod_vendedor)
  produto.save()
  return HttpResponseRedirect(reverse('indexproduto'))
