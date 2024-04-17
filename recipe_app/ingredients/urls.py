from django.urls import path
from .views import ingredients

app_name = 'ingredients'

urlpatterns = [
    path('', ingredients),
]