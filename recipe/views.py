from django.shortcuts import render
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