from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe.html"
    context_object_name = "recipe"


class RecipesListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"
    context_object_name = "recipes_list"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipes-list')


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "recipe_image_form.html"

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe', kwargs={'pk': self.kwargs['pk']})
