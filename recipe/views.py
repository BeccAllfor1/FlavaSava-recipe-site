from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Avg
from .models import Recipe, Category, Review, Profile
from .forms import UserRegisterForm, ProfileForm, RecipeForm, CategoryForm, ReviewForm, RecipeSearchForm

def home(request):
    recipes = Recipe.objects.all().order_by('-created_at')[:6]
    return render(request, 'home.html', {'recipes': recipes})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created! Please complete your profile.')
            return redirect('create_profile')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})