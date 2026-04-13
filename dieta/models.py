from django.db import models

class Alimento(models.Model):
    nome = models.CharField(max_length=100)
    calorias = models.IntegerField()
    proteinas = models.FloatField(help_text="Em gramas")
    carboidratos = models.FloatField(help_text="Em gramas")
    gorduras = models.FloatField(help_text="Em gramas")

    def __str__(self):
        return self.nome
