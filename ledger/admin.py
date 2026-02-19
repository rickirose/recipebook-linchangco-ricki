from django.contrib import admin
from .models import Recipe, RecipeIngredient

class RecipeInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInLine,]
    search_fields = ('name',)

admin.site.register(Recipe, RecipeAdmin)
