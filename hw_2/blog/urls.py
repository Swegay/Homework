from django.contrib import admin
from django.urls import path

from .views import get_ingex_page, get_article_details

urlpatterns = [
    path('', get_ingex_page),
    path('article/<int:pk>', get_article_details)
]