from django.urls import path
from . import views

app_name = 'framework'
urlpatterns = [
    path('', views.index, name='index'),
    path('evaluacion', views.evaluacion, name='evaluacion'),
    path('resultados', views.resultados, name='resultados'),
    path('registrar', views.register, name='register'),
    path('login', views.v_login, name='login'),
    path('logout', views.v_logout, name='logout'),
]