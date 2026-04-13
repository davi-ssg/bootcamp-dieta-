from django.db import models
from django.contrib.auth.models import User
import datetime

# Tabela para registrar o Peso Diário
class RegistroPeso(models.Model):
    # Relaciona o peso ao usuário logado. Se o usuário for apagado, os registros também são (CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(default=datetime.date.today)
    peso = models.FloatField(help_text="Seu peso em kg")

    def __str__(self):
        return f"{self.usuario.username} - {self.peso}kg em {self.data}"

# Tabela para registrar os Alimentos do dia
class RegistroAlimento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(default=datetime.date.today)
    nome_alimento = models.CharField(max_length=150, help_text="Ex: 2 Ovos mexidos com pão")
    calorias = models.IntegerField(help_text="Quantidade de calorias")

    def __str__(self):
        return f"{self.usuario.username} - {self.nome_alimento} ({self.calorias} kcal)"