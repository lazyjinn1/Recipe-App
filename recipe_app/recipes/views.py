from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import SearchRecipeForm

@login_required
def search_view(request):
    if request.method == 'POST':
        form = SearchRecipeForm(request.POST)
        if form.is_valid():
            filters = {}
            recipe_name = form.cleaned_data.get('recipe_name')
            ingredient = form.cleaned_data.get('ingredient')
            difficulty = form.cleaned_data.get('difficulty')
            max_cooking_time = form.cleaned_data.get('max_cooking_time')
            min_cooking_time = form.cleaned_data.get('min_cooking_time')

            if recipe_name:
                filters['recipe_name__icontains'] = recipe_name
            if ingredient:
                filters['ingredients__icontains'] = ingredient
            if difficulty:
                filters['difficulty'] = difficulty
            if max_cooking_time:
                filters['cooking_time__lte'] = max_cooking_time
            if min_cooking_time:
                filters['cooking_time__gte'] = min_cooking_time

            recipes = Recipe.objects.filter(**filters)
            print('Recipes: ', recipes)
            return render(request, 'recipes/recipes_search.html', {'recipes': recipes, 'form': form})
    else:
        form = SearchRecipeForm()
    return render(request, 'recipes/recipes_search.html', {'form': form})

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'
