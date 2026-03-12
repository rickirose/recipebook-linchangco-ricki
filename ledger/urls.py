from django.urls import path
from .views import RecipesListView, RecipeView, RecipeCreateView, RecipeImageCreateView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name="recipes-list"),
    path('recipe/<int:pk>/', RecipeView.as_view(), name="recipe"),
    path('recipe/add', RecipeCreateView.as_view(), name="recipe-add"),
    path('recipe/<int:pk>/add_image',
         RecipeImageCreateView.as_view(), name="recipe-image-add"),
]
