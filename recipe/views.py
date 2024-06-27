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

    @login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your profile has been created!')
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

    @login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

    def recipe_list(request):
    form = RecipeSearchForm(request.GET)
    recipes = Recipe.objects.all()

    if form.is_valid():
        if form.cleaned_data['search_query']:
            recipes = recipes.filter(title__icontains=form.cleaned_data['search_query'])
        if form.cleaned_data['category']:
            recipes = recipes.filter(categories=form.cleaned_data['category'])
        if form.cleaned_data['difficulty']:
            recipes = recipes.filter(difficulty=form.cleaned_data['diffic