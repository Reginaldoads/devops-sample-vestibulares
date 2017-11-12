"""
Definition of models.
"""

from django.db import models

class Curso(models.Model):
  nome = models.CharField(max_length=200)
  periodo = models.CharField(max_length=50)
  instituicao = models.CharField(max_length=200)

# Create your models here.
