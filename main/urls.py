from django.urls import path

from main.views import contacts, home

app_name = 'main'
urlpatterns = [
    path('contacts/', contacts, name='contact_page'),
    path('', home, name='main_page')
]
