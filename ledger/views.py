from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe


class RecipeView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe.html"
    context_object_name = "recipe"


class RecipesListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"
    context_object_name = "recipes_list"
