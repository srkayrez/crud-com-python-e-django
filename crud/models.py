from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contatos(models.Model):
    tipo = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    numero = models.IntegerField(max_length=50)