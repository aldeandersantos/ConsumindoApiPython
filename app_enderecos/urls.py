from django.urls import path
from .views import EnderecoAPIView

urlpatterns = [
    path('endereco/<str:cep>/', EnderecoAPIView.as_view(), name='endereco_api'),
]