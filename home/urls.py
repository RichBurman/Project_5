from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('walking-packages/', views.walking_packages, name='walking_packages'),
    path('about-us/', views.about_us, name='about_us'),
    path('gallery/', views.gallery, name='gallery'),
    path('reviews/', views.reviews, name='reviews'),
]
