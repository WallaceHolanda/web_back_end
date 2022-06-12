from django.db import models

class Vendedores(models.Model):
  nome = models.CharField(max_length=255)
  documento = models.CharField(max_length=18)
  endereco = models.CharField(max_length=255)
  telefone = models.CharField(max_length=12)
  banco = models.CharField(max_length=50)
  conta = models.CharField(max_length=10)
  email = models.CharField(max_length=100)
  senha = models.CharField(max_length=25)
