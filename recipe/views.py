from django.shortcuts import render
from .recipe import Recipe

def home(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'recipe/home.html', context)


def about(request):
    return render(request, 'recipe/about.html', {'title': 'About'})