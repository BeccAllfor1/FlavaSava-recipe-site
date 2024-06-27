from django.contrib import admin
from .models import Recipe, Category, Review, Profile


#Register your models below

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Profile)