from django.contrib import admin
from .models import tab_cliente, tab_dependente

class ListViewCliente(admin.ModelAdmin):
    list_display=('nomeCliente', 'cpf', 'telefone')

# Register your models here.
admin.site.register(tab_cliente, ListViewCliente)
admin.site.register(tab_dependente)