from django.http import HttpResponse
from django.template import loader
from .models import Produtos

def indexproduto(request):
  listaProdutos = Produtos.objects.all().values()
  template = loader.get_template('indexProdutos.html')
  context = {
    'listaProdutos': listaProdutos,
  }
  return HttpResponse(template.render(context, request))
