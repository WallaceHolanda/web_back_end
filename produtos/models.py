from django.db import models

class Produtos(models.Model):
  nome = models.CharField(max_length=100)
  vendedor = models.CharField(max_length=255)
  valor = models.CharField(max_length=20)
  imagem = models.CharField(max_length=200)
