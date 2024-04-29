from django.urls import path
from .views import RecipeListView, RecipeDetailView, search_view

app_name = 'recipes'

urlpatterns = [
    path('home', RecipeListView.as_view(), name='home'),
    path('search', search_view, name='recipes_search'),
    path('<pk>', RecipeDetailView.as_view(), name='detail')
]