from django.urls import path
from .views import RecipesListView, RecipeView

urlpatterns = [
    path('', RecipesListView.as_view(), name="recipes_list"),
    path('<int:pk>/', RecipeView.as_view(), name="recipe"),
]