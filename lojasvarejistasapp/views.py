from django.shortcuts import render, HttpResponse, redirect
from .models import tab_cliente, tab_dependente, tab_fornecedor, tab_inventario, tab_item, tab_loja, tab_pedido, tab_produto
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.

##############################################
#                  HOME
##############################################
def home(request):
    return render(request, 'home.html')


##############################################
#                  CLIENTES
##############################################
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


##############################################
#                 DEPENDENTES
##############################################
def dependente(request):
    dependentes = tab_dependente.objects.all()
    clientes = tab_cliente.objects.all()
    context = {'dependentes':dependentes, 'clientes':clientes}
    return render(request, 'cad_dependente.html', context)

def cadastrar_dependente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        parentesco = request.POST.get('parentesco') 
        cliente_id = request.POST.get('cliente')

        cliente = get_object_or_404(tab_cliente, pk=cliente_id)

        novo_dependente = tab_dependente(
            nomeDependente=nome,
            parentesco=parentesco,
            Cliente=cliente
        )
        try:
            novo_dependente.save()
            messages.success(request, 'Dependente cadastrado com sucesso!')
        except Exception as e:
            messages.error(request, f'{e}')

    dependentes = tab_dependente.objects.all()
    clientes = tab_cliente.objects.all()
    context = {'dependentes':dependentes, 'clientes':clientes}
    return render(request, 'cad_dependente.html', context=context)

def excluir_dependente(request, dependente_id):
    dependente = tab_dependente.objects.get(id=dependente_id)
    try:
        dependente.delete()
        messages.success(request, 'Excluido com sucesso!')
    except Exception as e:
        messages.error(request, f'{e}')  

    dependentes = tab_dependente.objects.all()
    clientes = tab_cliente.objects.all()
    context = {'dependentes':dependentes, 'clientes':clientes}
    return render(request, 'cad_dependente.html', context=context)

def editar_dependente(request, dependente_id):
    dependente = get_object_or_404(tab_dependente, id=dependente_id)
    clientes = tab_cliente.objects.all()

    if request.method == 'POST':
        try:
                nome = request.POST.get('nome')
                parentesco = request.POST.get('parentesco')
                cliente_id = request.POST.get('cliente')

                cliente = get_object_or_404(tab_cliente, pk=cliente_id)

                dependente.nomeDependente = nome
                dependente.parentesco = parentesco
                dependente.Cliente = cliente

                dependente.save()
                messages.success(request, 'Dependente editado com sucesso!')
                # Recarregando dependente após salvar as mudanças
                dependente = get_object_or_404(tab_dependente, id=dependente_id)
                return redirect('dependente')  # Redirecionar para a página correta após a edição
        except Exception as e:
            messages.error(request, f'{e}')  
    
    dependentes =  tab_dependente.objects.all()   
    context = {'dependente': dependente, 'clientes': clientes, 'dependentes':dependentes}
    return render(request, 'cad_dependente.html', context=context)


##############################################
#                 PRODUTOS
##############################################
def produto(request):
    return render(request, 'cad_produto.html')


##############################################
#                FORNECEDOR
##############################################
def fornecedor(request):
    return render(request, 'cad_fornecedor.html')


##############################################
#                  LOJA
##############################################
def loja(request):
    lojas = tab_loja.objects.all()
    context = {'lojas':lojas}
    return render(request, 'cad_loja.html', context)

def cadastrar_loja(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        seg_sex = request.POST.get('seg_sex')
        sab = request.POST.get('sab')
        dom = request.POST.get('dom')

        # Criando uma instância do modelo tab_loja com os dados recebidos
        novo_loja = tab_loja(
            nomeLoja = nome,
            endereco = endereco,
            seg_sex = seg_sex,
            sab = sab,
            dom = dom
        )
        try:
            novo_loja.save()
            messages.success(request, 'Loja cadastrado com sucesso!')
        except Exception as e:
            messages.error(request, f'{e}')

    lojas = tab_loja.objects.all()
    context = {'lojas':lojas}

    return render(request, 'cad_loja.html', context)

def excluir_loja(request):
    lojas = tab_loja.objects.all()
    context = {'lojas':lojas}
    return render(request, 'cad_loja.html', context)

def editar_loja(request):
    lojas = tab_loja.objects.all()
    context = {'lojas':lojas}
    return render(request, 'cad_loja.html', context)