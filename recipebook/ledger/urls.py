from django.urls import path
from . import views
from .views import recipe_list

urlpatterns = [
    path('<int:id>', recipe_list, name='recipe-list'),
    path('recipe/1/', views.recipe_one, name='recipe-one'),
    path('recipe/2/', views.recipe_two, name='recipe-two'),
]

app_name = 'ledger'