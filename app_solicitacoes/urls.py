from django.urls import path
from .views import obter_enderecos

urlpatterns = [
    path('obter_enderecos/<str:cep>/', obter_enderecos, name='obter_enderecos'),
]