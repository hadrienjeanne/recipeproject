from django.conf import settings
from django.db import models
from .recipe import Recipe

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(default='')