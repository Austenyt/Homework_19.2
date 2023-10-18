from django.urls import path

from main.views import contacts, home

urlpatterns = [
    path('', contacts),
    path('', home)
]