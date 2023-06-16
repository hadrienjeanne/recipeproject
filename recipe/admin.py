from django.contrib import admin
from .recipe import Recipe
from .ingredient import Ingredient
from .review import Review


# Register your models here.
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Ingredient)