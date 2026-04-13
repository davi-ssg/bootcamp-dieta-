from django.contrib import admin
from django.urls import path, include
from dieta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')), # Ativa o login do Django
    path('', views.home, name='home'), # Nossa tela principal
]