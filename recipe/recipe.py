from django.conf import settings
from django.db import models
from django.utils import timezone
from .ingredient import Ingredient

class Recipe(models.Model):
    name = models.CharField(max_length=256)
    total_time = models.PositiveIntegerField(default=0)
    cooking_time = models.PositiveIntegerField(default=0)
    description = models.TextField(default='')
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField(default='')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    date_posted = models.DateField(default=timezone.now)

    @staticmethod
    def get_recipe_by_name(name):
        try: 
            return Recipe.objects.get(name=name)
        except:
            return False
        
    @staticmethod
    def get_all_recipes():
        return Recipe.objects.all()
    

    def __str__(self) -> str:
        return self.name
