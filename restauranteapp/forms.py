from django import forms
from .models import Ingredientes, MenuItens, Carrinho

class IngredientesCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredientes
        fields = "__all__"

class MenuItensCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItens
        fields = "__all__"

class CarrinhoCreateForm(forms.ModelForm):
    class Meta:
        model = Carrinho
        fields = "__all__"
        