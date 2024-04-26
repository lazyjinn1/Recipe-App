from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Recipe
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import SearchRecipeForm
from .utils import get_recipename_from_id, get_chart
import pandas as pd # type: ignore


@login_required
def search_view(request):
    form = SearchRecipeForm(request.POST or None)
    recipes_df = None
    chart = None   

    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        chart_type = request.POST.get('chart_type')

        qs=Recipe.objects.filter(recipe_name=recipe_name)
        if qs:
           recipes_df=pd.DataFrame(qs.values()) 
           recipes_df['id'].apply(get_recipename_from_id)
           chart=get_chart(chart_type, recipes_df, labels=recipes_df['cooking_time'].values)

           recipes_df=recipes_df.to_html()

    context={
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart
    }
    
    return render(request, 'recipes/recipes_search.html', context)

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):                     
   model = Recipe                                        
   template_name = 'recipes/recipes_detail.html'  