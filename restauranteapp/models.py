from django.db import models

# Create your models here.
#cria o modelo dos ingredientes
class Ingredientes(models.Model):
    nome = models.CharField(max_length=30,default='', verbose_name="Nome")
    quant = models.IntegerField(default=0, verbose_name="Quantidade")
    preco = models.FloatField(default=0.0, verbose_name="Preço")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return '/'

#cria o modelo dos itens do menu
class MenuItens(models.Model):  
    nome = models.CharField(max_length=30, verbose_name="Nome")
    #quero que ingrediente mostre o nome e a quantidade do ingrediente
    ingredientes = models.ForeignKey(Ingredientes,on_delete=models.CASCADE, verbose_name="Ingredientes")
    preco = models.FloatField(default=0.0, verbose_name="Preço")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return '/'

#cria o modelo dos itens no carrinho
class Carrinho(models.Model):
    nome = models.CharField(max_length=30)
    produto = models.ForeignKey(MenuItens,on_delete=models.CASCADE)
    #deve se incrementar a cada produto adicionado
    preco = models.FloatField(default=0.0)