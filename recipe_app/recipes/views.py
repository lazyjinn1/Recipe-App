from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import SearchRecipeForm
from .utils import get_countOfAll_recipes

@login_required
def search_view(request):
    form = SearchRecipeForm(request.POST or None)
    recipes_df = None

    if request.method == 'POST':
        search_name = request.POST.get('recipe_name')
        search_by_ingredient = request.POST.get('ingredients')
        search_difficulty = request.POST.get('difficulty')
        search_max_cooking_time = request.POST.get('max_cooking_time')
        search_min_cooking_time = request.POST.get('min_cooking_time')

        all_recipes_qs = Recipe.objects.all()
        if all_recipes_qs:
            filters = {}
            if search_name:
                filters['recipe_name'] = search_name
            if search_by_ingredient:
                filters['ingredients_contains'] = search_by_ingredient
            if search_difficulty:
                filters['difficulty'] = search_difficulty
            if search_max_cooking_time:
                filters['cooking_time_max'] = search_max_cooking_time
            if search_min_cooking_time:
                filters['cooking_time_min'] = search_min_cooking_time

            filtered_recipes = all_recipes_qs.filter(**filters)
            recipes_df = filtered_recipes.values()

    context = {
        'form': form,
        'recipes_df': recipes_df,
    }

    return render(request, 'recipes/recipes_search.html', context)

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'
