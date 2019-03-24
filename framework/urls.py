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
    path('objetivos', views.v_learning_objectives, name='objetivos'),
    path('listobj', views.list_objectives, name='list_objetivos'),
    path('editar/<int:codigo>/', views.v_learning_objectives_edit, name='edit_objetivos'), 
]