from django.http import HttpResponse
from django.template import loader
from .models import Vendedores

def index(request):
  listaVendedores = Vendedores.objects.all().values()
  template = loader.get_template('indexVendedores.html')
  context = {
    'listaVendedores': listaVendedores,
  }
  return HttpResponse(template.render(context, request))
