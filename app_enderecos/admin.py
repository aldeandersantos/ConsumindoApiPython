# app_enderecos/admin.py
from django.contrib import admin
from .models import Endereco

class ListandoEnderecos(admin.ModelAdmin):
    list_display = ("cep", "street", "endereco_ativo")
    list_display_links = ("cep", "street")
    search_fields = ("cep",)
    list_filter = ("state", "endereco_ativo",)
    list_editable = ("endereco_ativo",)

admin.site.register(Endereco,ListandoEnderecos)

