from django.urls import path
from .views import EnderecoAPIView

urlpatterns = [
    # GET
    path('endereco/<str:cep>/', EnderecoAPIView.as_view(), name='endereco_api'),

    # POST
    path('endereco/', EnderecoAPIView.as_view(), name='create_endereco_api'),

    # PUT
    path('endereco/<str:cep>/', EnderecoAPIView.as_view(), name='update_endereco_api'),

    # DELETE
    path('endereco/<str:cep>/', EnderecoAPIView.as_view(), name='delete_endereco_api'),
]