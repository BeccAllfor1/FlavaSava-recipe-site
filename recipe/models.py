from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#profile model
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile/')#, null=True, blank=Treu)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')




# Recipe model
class Recipe(models.Model):
     recipe_id = models.AutoField(primary_key=True)
     difficulty = models.CharField(max_length=200)
     ingredients = models.TextField()
     cooking_time = models.DurationField()
     serves = models.IntegerField()
     steps = models.TextField()
     image = models.ImageField(upload_to='recipe/', null=True, blank=True)
     created_by = models.CharField(max_length=200)
     created_at = models.DateTimeField(auto_now_add=True)
     profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='recipe')

# category model
class Category(models.Model):
    Category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='category') 

# review model
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    rating = models.IntegerField()
    body = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='review')
   

