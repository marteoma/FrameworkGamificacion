from django.urls import path
from . import views

app_name = 'administration'
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.current, name='current')
]
