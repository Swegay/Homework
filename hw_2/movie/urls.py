from django.contrib import admin
from django.urls import path

from .views import get_ingex_page, get_movie_details

urlpatterns = [
    path('', get_ingex_page),
    path('movie/<int:pk>', get_movie_details)
]