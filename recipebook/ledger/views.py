from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Profile, Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    context_object_name = 'recipe'
