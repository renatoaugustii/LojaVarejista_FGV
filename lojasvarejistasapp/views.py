from django.shortcuts import render, HttpResponse

# Create your views here.
def cadastrar_cliente(request):

    return render(request, 'clientes.html')