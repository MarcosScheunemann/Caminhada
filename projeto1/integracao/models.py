from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Video(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=1500)
    url = models.CharField(max_length=300)
