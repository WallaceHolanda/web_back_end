from django.db import models
class Clientes(models.Model):
  nome = models.CharField(max_length=255)
  cpf = models.CharField(max_length=15)
  nascimento = models.CharField(max_length=11)
  email = models.CharField(max_length=255)
  senha = models.CharField(max_length=50)

# Create your models here.
