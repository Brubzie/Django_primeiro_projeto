from typing import Any
from django.db import models

# Create your models here.
# Irá "cuspir" a informação no meu Banco de Dados

# Perguntas
class Question(models.Model):
    question_text = models.CharField(max_lenght = 200) # Campo de carácteres 
    pub_date = models.DateTimeField('date publishied') # Campo de data

# Escolha
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_lenght = 200)
    votes = models.IntegerField(default = 0)
