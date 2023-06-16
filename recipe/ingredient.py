from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to="ingredients", default="ingredients/default.jpg")
    calories = models.PositiveIntegerField(default=0)
    
    @staticmethod
    def get_ingredient_by_name(name):
        try:
            return Ingredient.objects.get(name=name)
        except:
            return False
        
    @staticmethod
    def get_all_ingredients():
        return Ingredient.objects.all()

    def __str__(self) -> str:
        return self.name
    