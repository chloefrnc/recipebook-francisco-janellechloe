from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeAddView, RecipeImageView

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name="recipe_list"),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add/', RecipeAddView.as_view(), name="recipe_add"),
    path('recipe/<int:pk>/ass_image/', RecipeImageView.as_view(), name='recipe_image')
]

app_name = 'ledger'
