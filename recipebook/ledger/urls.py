from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeAddView

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name="recipe_list"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add/', RecipeAddView.as_view, name="recipe_add")
]

app_name = 'ledger'
