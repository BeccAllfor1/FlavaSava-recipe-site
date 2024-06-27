from django.urls import path
from .views import recipe_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
     path('new/', recipe_create, name='recipe_create'),
]