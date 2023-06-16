from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipe-home'),
    path('about/', views.about, name='recipe-about'),
]