from typing import Any
from django.shortcuts import render, get_object_or_404
from .models import Ingredientes, MenuItens, Carrinho
from .forms import IngredientesCreateForm, MenuItensCreateForm, CarrinhoCreateForm
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.
def home(request):
    return render(request, "restauranteapp/home.html")

def ingredientes(request):
    all_itens = Ingredientes.objects.all()
    context = {'itens':all_itens, 'botao':'voltar'}
    return render(request, "restauranteapp/ingredientes.html", context)

def menuitens(request):
    all_itens = MenuItens.objects.all()
    context = {'itens':all_itens, 'botao':'voltar'}
    return render(request, "restauranteapp/menu_itens.html", context)

class IngredientesCreateView(CreateView):
    model = Ingredientes
    form_class = IngredientesCreateForm
    template_name = 'restauranteapp/ingredientes_create_form.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['botao'] = 'Voltar'
        return context

class MenuItensCreateView(CreateView):
    model = MenuItens
    form_class = MenuItensCreateForm
    template_name = 'restauranteapp/menu_itens_create_form.html'