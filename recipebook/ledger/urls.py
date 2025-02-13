from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe-list'),
    path('recipe/1/', views.recipe_one, name='recipe-one'),
    path('recipe/2/', views.recipe_two, name='recipe-two'),
]

app_name = 'ledger'