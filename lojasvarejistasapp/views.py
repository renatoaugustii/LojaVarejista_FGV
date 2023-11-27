from django.shortcuts import render, HttpResponse
from .models import tab_cliente, tab_dependente
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    return render(request, 'home.html')

def cliente(request):
    clientes = tab_cliente.objects.all()
    context = {'clientes':clientes}
    return render(request, 'cad_cliente.html', context)

def cadastrar_cliente(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf') 
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco') 
        # Criando uma instância do modelo tab_cliente com os dados recebidos
        novo_cliente = tab_cliente(
            nomeCliente=nome,
            cpf=cpf,
            telefone=telefone,
            endereco=endereco,
            programaPTS=0, #valor padrão para o programaPTS
            totalPontos=0  #valor padrão para totalPontos
        )
        try:
            novo_cliente.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
        except Exception as e:
            messages.error(request, f'{e}')

    clientes = tab_cliente.objects.all()
    context = {'clientes':clientes}

    return render(request, 'cad_cliente.html', context)

def excluir_cliente(request, cliente_id):
    cliente = tab_cliente.objects.get(id=cliente_id)

    try:
        cliente.delete()
        messages.success(request, 'Cliente excluido com sucesso!')
    except Exception as e:
        messages.error(request, f'{e}')        

    #Busca todos os clientes do banco de dados já cadastrados.
    clientes = tab_cliente.objects.all()
    context = {'clientes':clientes}

    return render(request, 'cad_cliente.html', context)

def editar_cliente(request, cliente_id):

    cliente = get_object_or_404(tab_cliente, id=cliente_id)
    clientes = tab_cliente.objects.all()

    if request.method == 'POST':
        cliente.nomeCliente = request.POST.get('nome')
        cliente.cpf = request.POST.get('cpf')
        cliente.telefone = request.POST.get('telefone')
        cliente.endereco = request.POST.get('endereco')
        # Atualize os outros campos conforme necessário

        cliente.save()  # Salva as alterações no banco de dados

        context = {'clientes': clientes, 'cliente': cliente}
        return render(request, 'cad_cliente.html', context)

    context = {'clientes': clientes, 'cliente': cliente}
    return render(request, 'cad_cliente.html', context)



def dependente(request):
    dependentes = tab_dependente.objects.all()
    clientes = tab_cliente.objects.all()
    context = {'dependentes':dependentes, 'clientes':clientes}

    return render(request, 'cad_dependente.html', context)





def produto(request):
    return render(request, 'cad_produto.html')

def fornecedor(request):
    return render(request, 'cad_fornecedor.html')

def loja(request):
    return render(request, 'cad_loja.html')
