from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Endereco
from .serializers import EnderecoSerializer

class EnderecoAPIView(APIView):
    def get(self, request, cep, format=None):
        endereco = Endereco.objects.get(cep=cep)
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)
