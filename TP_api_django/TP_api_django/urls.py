"""
URL configuration for TP_api_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from my_app import views
from . import views

urlpatterns = [
    path('api/egg_groups/', views.EggGroupList.as_view()),
    path('api/egg_groups/<int:pk>/', views.EggGroupDetail.as_view()),
    
    path('api/items/', views.ItemList.as_view()),
    path('api/items/<int:pk>/', views.ItemDetail.as_view()),
    
    path('api/locations/', views.LocationList.as_view()),
    path('api/locations/<int:pk>/', views.LocationDetail.as_view()),
    
    path('api/moves/', views.MoveList.as_view()),
    path('api/moves/<int:pk>/', views.MoveDetail.as_view()),
    
    path('api/pokemon/', views.PokemonList.as_view()),
    path('api/pokemon/<int:pk>/', views.PokemonDetail.as_view()),
    
    path('api/pokemon_egg_groups/', views.PokemonEggGroupList.as_view()),
    path('api/pokemon_egg_groups/<int:pk>/', views.PokemonEggGroupDetail.as_view()),
    
    path('api/pokemon_form_generations/', views.PokemonFormGenerationList.as_view()),
    path('api/pokemon_form_generations/<int:pk>/', views.PokemonFormGenerationDetail.as_view()),
    
    path('api/pokemon_moves/', views.PokemonMoveList.as_view()),
    path('api/pokemon_moves/<int:pk>/', views.PokemonMoveDetail.as_view()),
    
    path('api/pokemon_stats/', views.PokemonStatList.as_view()),
    path('api/pokemon_stats/<int:pk>/', views.PokemonStatDetail.as_view()),
    
    path('api/pokemon_types/', views.PokemonTypeList.as_view()),
    path('api/pokemon_types/<int:pk>/', views.PokemonTypeDetail.as_view()),
    
    path('api/stats/', views.StatList.as_view()),
    path('api/stats/<int:pk>/', views.StatDetail.as_view()),
    
    path('api/types/', views.TypeList.as_view()),
    path('api/types/<int:pk>/', views.TypeDetail.as_view()),
]
