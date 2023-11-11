from django.db import models

# Create your models here.
class tab_cliente(models.Model):
    nomeCliente = models.CharField(max_length=60, blank=False)
    cpf = models.CharField(max_length=20,unique=True, blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=False, unique=True)
    endereco = models.CharField(max_length=30, blank=True)
    pontos = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.nomeCliente


class tab_dependente(models.Model):
    nomeDependente = models.CharField(max_length=60, blank=False)
    parentesco = models.CharField(max_length=60, blank=False)
    #ForeignKeys
    Cliente = models.ForeignKey(tab_cliente, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomeDependente

class tab_loja(models.Model):
    nomeLoja = models.CharField(max_length=60, blank=False)
    endereco = models.CharField(max_length=60, blank=False)
    seg_sex = models.CharField(max_length=60, blank=False)
    sab = models.CharField(max_length=60, blank=False)
    dom = models.CharField(max_length=60, blank=False)
    def __str__(self):    
        return self.nomeLoja

class tab_fornecedor(models.Model):
    nomeFornecedor = models.CharField(max_length=60, blank=False, unique=True)
    endereco = models.CharField(max_length=60, blank=False)
    def __str__(self):
        return self.nomeFornecedor

class tab_produto (models.Model):
    nomeProduto = models.CharField(max_length=60, blank=False)
    descricao = models.CharField(max_length=60, blank=False)
    tamanho = models.CharField(max_length=60, blank=False)
    mEmpacotamento = models.CharField(max_length=60, blank=True)
    codBarras = models.IntegerField(blank=False, null=False, unique=True)
    marca = models.CharField(max_length=60, blank=False)
    # ManytoMany Below
    fornecedores = models.ManyToManyField(tab_fornecedor)
    def __str__(self):    
        return self.nomeProduto

class tab_pedido(models.Model):
    choice_tipo_venda=(
        ('V','Virtual'),
        ('F','Fisico')
    )
    data = models.DateField(blank=False, null= False)
    tipo_venda = models.CharField(max_length=1, choices = choice_tipo_venda, blank=False, null=True)
    total_pedido = models.FloatField(default=0.0, blank=False, null=False)
    # ForeingKey Below
    Cliente = models.ForeignKey(tab_cliente, on_delete=models.CASCADE)
    Dependente = models.ForeignKey(tab_dependente, default= 0 ,blank=True, null=True ,on_delete=models.CASCADE)

    
class tab_item(models.Model):
    data = models.ForeignKey(tab_pedido, blank = False, null= False, on_delete=models.CASCADE)
    quantidade = models.IntegerField(blank=False, null=False)
    PrecoUnitario = models.FloatField(default=0.0, blank=False, null=False)
    subTotal = models.FloatField(default=0.0, blank=False, null=False)
    def __str__(self):    
        return self.quantidade