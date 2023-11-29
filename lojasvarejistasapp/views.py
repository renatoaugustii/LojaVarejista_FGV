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
    produtos = tab_produto.objects.all()
    lojas = tab_loja.objects.all()
    fornecedores = tab_fornecedor.objects.all()
    context = {'produtos':produtos, 'lojas':lojas, 'fornecedores':fornecedores}
    return render(request, 'cad_produto.html', context)




def cadastrar_produto(request):
    produtos = tab_produto.objects.all()
    lojas = tab_loja.objects.all()
    fornecedores = tab_fornecedor.objects.all()
    context = {'produtos':produtos, 'lojas':lojas, 'fornecedores':fornecedores}
    return render(request, 'cad_produto.html', context)

def editar_produto(request):
    produtos = tab_produto.objects.all()
    lojas = tab_loja.objects.all()
    fornecedores = tab_fornecedor.objects.all()
    context = {'produtos':produtos, 'lojas':lojas, 'fornecedores':fornecedores}
    return render(request, 'cad_produto.html', context)

def excluir_produto(request,produto_id):
    produto = tab_produto.objects.get(id=produto_id)
    try:
        produto.delete()
        messages.success(request, 'produto excluido com sucesso!')
    except Exception as e:
        messages.error(request, f'{e}')        
    #Busca todos os produtos do banco de dados já cadastrados.
    produtos = tab_produto.objects.all()
    lojas = tab_loja.objects.all()
    fornecedores = tab_fornecedor.objects.all()
    context = {'produtos':produtos, 'lojas':lojas, 'fornecedores':fornecedores}
    return render(request, 'cad_produto.html', context)

##############################################
#                FORNECEDOR
##############################################
def fornecedor(request):
    fornecedores = tab_fornecedor.objects.all()
    context = {'fornecedores':fornecedores}
    return render(request, 'cad_fornecedor.html', context)

def cadastrar_fornecedor(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco') 

        # Criando uma instância do modelo tab_fornecedor com os dados recebidos
        novo_fornecedor = tab_fornecedor(
            nomeFornecedor=nome,
            endereco=endereco,
        )
        try:
            novo_fornecedor.save()
            messages.success(request, 'fornecedor cadastrado com sucesso!')
        except Exception as e:
            messages.error(request, f'{e}')

    fornecedores = tab_fornecedor.objects.all()
    context = {'fornecedores':fornecedores}
    return render(request, 'cad_fornecedor.html', context)

def editar_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(tab_fornecedor, id=fornecedor_id)
    fornecedores = tab_fornecedor.objects.all()

    if request.method == 'POST':
        try:
                nome = request.POST.get('nome')
                endereco= request.POST.get('endereco')

                fornecedor = get_object_or_404(tab_fornecedor, pk=fornecedor_id)

                fornecedor.nomeFornecedor = nome
                fornecedor.endereco= endereco

                fornecedor.save()
                messages.success(request, 'fornecedor editado com sucesso!')
                # Recarregando fornecedor após salvar as mudanças
                fornecedor = get_object_or_404(tab_fornecedor, id=fornecedor_id)
                return redirect('fornecedor')  # Redirecionar para a página correta após a edição
        except Exception as e:
            messages.error(request, f'{e}')  
    
    fornecedors =  tab_fornecedor.objects.all()   
    context = {'fornecedor': fornecedor, 'fornecedores': fornecedores, 'fornecedors':fornecedors}
    return render(request, 'cad_fornecedor.html', context=context)

def excluir_fornecedor(request, fornecedor_id):
    fornecedor = tab_fornecedor.objects.get(id=fornecedor_id)
    try:
        fornecedor.delete()
        messages.success(request, 'Excluido com sucesso!')
    except Exception as e:
        messages.error(request, f'{e}')  

    fornecedores = tab_fornecedor.objects.all()
    clientes = tab_cliente.objects.all()
    context = {'fornecedores':fornecedores, 'clientes':clientes}
    return render(request, 'cad_fornecedor.html', context=context)

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

def excluir_loja(request, loja_id):

    loja = tab_loja.objects.get(id=loja_id)
    try:
        loja.delete()
        messages.success(request, 'loja excluido com sucesso!')
    except Exception as e:
        messages.error(request, f'{e}')        
    #Busca todos os lojas do banco de dados já cadastrados.
    lojas = tab_loja.objects.all()
    context = {'lojas':lojas}
    return render(request, 'cad_loja.html', context)

def editar_loja(request, loja_id):

    loja = get_object_or_404(tab_loja, id=loja_id)
    lojas = tab_loja.objects.all()

    if request.method == 'POST':
        loja.nomeLoja = request.POST.get('nome')
        loja.endereco = request.POST.get('endereco')
        loja.seg_sex = request.POST.get('seg_sex')
        loja.sab = request.POST.get('sab')
        loja.dom = request.POST.get('dom')
        # Atualize os outros campos conforme necessário

        loja.save()  # Salva as alterações no banco de dados

        context = {'lojas': lojas, 'loja': loja}
        return redirect('loja')  # Redirecionar para a página correta após a edição

    context = {'lojas': lojas, 'loja': loja}
    return render(request, 'cad_loja.html', context)