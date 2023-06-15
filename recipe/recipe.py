from django.db import models
from .ingredient import Ingredient

class Recipe(models.Model):
    name = models.CharField(max_length=256)
    total_time = models.PositiveIntegerField(default=0)
    cooking_time = models.PositiveIntegerField(default=0)
    description = models.TextField(default='')
    ingredients = models.ManyToManyField(Ingredient, on_delete=models.CASCADE)
    instructions = models.TextField(default='')