from django.urls import path
from .views import RecipesListView, RecipeView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name="recipes-list"),
    path('<int:pk>/', RecipeView.as_view(), name="recipe"),
]
