from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RegistroPeso, RegistroAlimento
from .forms import PesoForm, AlimentoForm

# A tag @login_required expulsa quem não estiver logado e manda pra tela de login
@login_required 
def home(request):
    # Puxa apenas o histórico do usuário que está logado
    pesos = RegistroPeso.objects.filter(usuario=request.user).order_by('-data')
    alimentos = RegistroAlimento.objects.filter(usuario=request.user).order_by('-data')

    # Verifica se o usuário apertou algum botão de "Salvar"
    if request.method == 'POST':
        if 'btn_peso' in request.POST:
            form_peso = PesoForm(request.POST)
            if form_peso.is_valid():
                peso = form_peso.save(commit=False)
                peso.usuario = request.user # Associa o peso ao usuário logado
                peso.save()
                return redirect('home') # Recarrega a página

        elif 'btn_alimento' in request.POST:
            form_alimento = AlimentoForm(request.POST)
            if form_alimento.is_valid():
                alimento = form_alimento.save(commit=False)
                alimento.usuario = request.user
                alimento.save()
                return redirect('home')

    # Se não apertou botão nenhum, apenas carrega os formulários vazios
    form_peso = PesoForm()
    form_alimento = AlimentoForm()

    return render(request, 'dieta/home.html', {
        'pesos': pesos,
        'alimentos': alimentos,
        'form_peso': form_peso,
        'form_alimento': form_alimento
    })