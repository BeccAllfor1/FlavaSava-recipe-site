# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Profile, Recipe, Category, Review 
# from .forms import ProfileForm, RecipeForm, CategoryForm, RecipeForm
# from django.http import HttpResponse
# # Create your views here.

# # def my_recipe(request):
# #  return HttpResponse("Hello, flavasava!")

# #@login_required
# def recipe_list(request):
#     recipes = Recipe.objects.filter(user=request.user)
#     return render(request, 'base.html', {'recipes':recipes}) 


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
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profile.html', {'profile': profile})

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
            recipes = recipes.filter(difficulty=form.cleaned_data['difficulty'])

    return render(request, 'recipe_list.html', {'recipes': recipes, 'form': form})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    reviews = recipe.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.recipe = recipe
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = ReviewForm()
    
    context = {
        'recipe': recipe,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'form': form
    }
    return render(request, 'recipe_detail.html', context)

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            form.save_m2m()  # Save many-to-many data
            messages.success(request, 'Your recipe has been created!')
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, created_by=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your recipe has been updated!')
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, created_by=request.user)
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Your recipe has been deleted!')
        return redirect('recipe_list')
    return render(request, 'delete_recipe.html', {'recipe': recipe})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.recipes.all()
    return render(request, 'category_detail.html', {'category': category, 'recipes': recipes})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New category has been created!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})