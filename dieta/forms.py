from django import forms
from .models import RegistroPeso, RegistroAlimento

class PesoForm(forms.ModelForm):
    class Meta:
        model = RegistroPeso
        fields = ['peso'] # Só pedimos o peso, o resto o sistema preenche sozinho

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = RegistroAlimento
        fields = ['nome_alimento', 'calorias']