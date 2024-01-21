from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Endereco
from .serializers import EnderecoSerializer
from .decorators import handle_erros

class EnderecoAPIView(APIView):
    @handle_erros
    def get(self, request, cep=None, format=None):
        if cep is None:
            raise ValueError("CEP não fornecido na solicitação.")
        endereco = Endereco.objects.get(cep=cep)
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)

    @handle_erros
    def post(self, request, cep=None, format=None):
        if cep is not None:
            raise ValueError("Deixe cep na URI vazia.")
        serializer = EnderecoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @handle_erros
    def put(self, request, cep=None, format=None):
        if cep is None:
            raise ValueError("CEP não fornecido na solicitação.")
        endereco = Endereco.objects.get(cep=cep)
        serializer = EnderecoSerializer(endereco, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @handle_erros
    def delete(self, request, cep=None, format=None):
        if cep is None:
            raise ValueError("CEP não fornecido na solicitação.")
        endereco = Endereco.objects.get(cep=cep)
        endereco.delete()
        return Response({"message": "Endereço deletado com sucesso."})