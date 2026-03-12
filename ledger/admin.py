from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, RecipeIngredient, Profile, RecipeImage


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine,]


class RecipeInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInLine, RecipeImageInline]
    search_fields = ('name',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
