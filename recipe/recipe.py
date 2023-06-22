from django.conf import settings
from django.db import models
from django.utils import timezone
from .ingredient import Ingredient

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, default='')
    total_time = models.PositiveIntegerField(default=0)
    cooking_time = models.PositiveIntegerField(default=0)
    nb_persons = models.PositiveIntegerField(default=0)
    description = models.TextField(default='')
    picture = models.ImageField(upload_to="recipes", default="recipes/default.jpg")
    ingredients = models.ManyToManyField(
            Ingredient, 
            through='RecipeIngredient',
            through_fields=('recipe','ingredient'),
        )
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
    


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()
    measuring_unit = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.recipe.name} <-> {self.ingredient.name}: {self.amount} {self.measuring_unit}"