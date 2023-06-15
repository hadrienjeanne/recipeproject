from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    calories = models.PositiveIntegerField(default=0)
    measuring_unit = models.CharField(max_length=64)
    