from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .recipe import Recipe

def home(request):
    recipes = Recipe.objects.all()
    paginator = Paginator(recipes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'recipes': page_obj
    }
    return render(request, 'recipe/home.html', context)

def about(request):
    return render(request, 'recipe/about.html', {'title': 'About'})

def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe.objects.all(), slug=slug)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe/detail.html', context)

def new_recipe(request):
    #todo, gérer la création du slug à partir du nom de la recette
    pass