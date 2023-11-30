from django.urls import path

from main.views import contacts, index

app_name = 'main'
urlpatterns = [
    path('contacts/', contacts, name='contact_page'),
    path('', index, name='main_page')
]
