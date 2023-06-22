from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='recipe-home'),
    path('about/', views.about, name='recipe-about'),
    path('recipe/new', views.new_recipe, name='recipe-new'),
    path('recipe/detail/<slug:slug>', views.recipe_detail, name='recipe-detail'),
]
# allowing media serve in debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)