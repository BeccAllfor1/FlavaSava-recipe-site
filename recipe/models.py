# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# #profile model
# class Profile(models.Model):
#     profile_id = models.AutoField(primary_key=True)
#     firstname = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='profile/')#, null=True, blank=Treu)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')




# # Recipe model
# class Recipe(models.Model):
#      recipe_id = models.AutoField(primary_key=True)
#      difficulty = models.CharField(max_length=200)
#      ingredients = models.TextField()
#      cooking_time = models.DurationField()
#      serves = models.IntegerField()
#      steps = models.TextField()
#      image = models.ImageField(upload_to='recipe/', null=True, blank=True)
#      created_by = models.CharField(max_length=200)
#      created_at = models.DateTimeField(auto_now_add=True)
#      profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='recipe')

# # category model
# class Category(models.Model):
#     Category_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='category') 

# # review model
# class Review(models.Model):
#     review_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200, unique=True)
#     rating = models.IntegerField()
#     body = models.TextField()
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='review')

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    firstname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.surname}"

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    ingredients = models.TextField()
    cooking_time = models.DurationField()
    serves = models.PositiveIntegerField()
    steps = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False)
    featured_image = models.ImageField(null=False)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    recipes = models.ManyToManyField(Recipe, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Review(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    body = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.rating}/5"

    class Meta:
        unique_together = ['recipe', 'user']
   

