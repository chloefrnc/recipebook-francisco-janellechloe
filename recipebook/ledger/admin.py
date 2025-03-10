from django.contrib import admin
from .models import Profile, Recipe, Ingredient, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]

admin.site.register(Profile)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
