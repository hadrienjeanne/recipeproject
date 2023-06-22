from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .recipe import Recipe
from .forms import RecipeForm

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
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RecipeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecipeForm()

    return render(request, "recipe/new_recipe.html", {"form": form})