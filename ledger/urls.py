from django.urls import path
from .views import ledger, recipe_list, recipe_1, recipe_2

urlpatterns = [
    path('', ledger, name='ledger'),
    path('recipes/list/', recipe_list, name='recipe-list'),
    path('recipes/recipe/1/', recipe_1, name='recipe-1'),
    path('recipes/recipe/2/', recipe_2, name='recipe-2'),
]