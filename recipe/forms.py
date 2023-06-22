from django import forms
from .ingredient import Ingredient
# from .recipe import Recipe

class RecipeForm(forms.Form):
    recipe_name = forms.CharField(label="Recipe name", max_length=128, required=True)
    total_time = forms.IntegerField(label="Total time", required=False)
    cooking_time = forms.IntegerField(label="Cooking time", required=False)
    nb_persons = forms.IntegerField(label="Number of persons", min_value=0, max_value=32, required=False)
    description = forms.CharField(label="description of the recipe", required=True)
    picture = forms.ImageField(label="Picture of the recipe", required=False)
    instructions = forms.CharField(label="Instructions", widget=forms.Textarea, required=True)
    # TODO: ajouter ingrédients et leurs quantités
    ingredients_list = [[x.id, x.name] for x in Ingredient.objects.all()]
    ingredients = forms.MultipleChoiceField(choices=ingredients_list, label="Ingredients", required=True)

# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['name', 'description', 'total_time', 'cooking_time', 'nb_persons', 'picture', 'ingredients', 'instructions']