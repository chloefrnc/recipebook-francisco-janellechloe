from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    context_object_name = 'recipe'
    redirect_field_name = 'accounts/login/'


class RecipeAddView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'ledger/recipe_add.html'
    redirect_field_name = 'accounts/login'
    form_class = RecipeForm


class RecipeImageView(CreateView):
    model = RecipeImage
    template_name = 'ledger/recipe_image.html'
    context_object_name = 'image'
    form_class = RecipeImageForm

    def get_pk(self):
        return self.objects.recipe.pk

    def get_success_url(self):
        return reverse_lazy(
            'ledger:recipe_list'
        )
