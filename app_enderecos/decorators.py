from rest_framework.response import Response
from rest_framework import status
from .models import Endereco

def handle_erros(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Endereco.DoesNotExist:
            return Response({"error": "Endereço não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return wrapper