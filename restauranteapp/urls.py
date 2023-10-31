from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingredientes/', views.ingredientes, name='ingredientes'),
    path('menu_itens/', views.menuitens, name='menuitens'),
    path('ingredientes/create', views.IngredientesCreateView.as_view(), name='ingredientescreate'),
    path('menu_itens/create', views.MenuItensCreateView.as_view(), name='menuitenscreate')
]