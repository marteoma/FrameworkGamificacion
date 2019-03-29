from django.urls import path
from . import views

app_name = 'framework'
urlpatterns = [
    path('', views.index, name='index'),    
    path('resultados', views.resultados, name='resultados'),
    path('registrar', views.register, name='register'),
    path('login', views.v_login, name='login'),
    path('logout', views.v_logout, name='logout'),
    path('objetivos/<int:assessment>', views.v_learning_objectives, name='objetivos'),
    path('listobj/<int:assessment>', views.list_objectives, name='list_objetivos'),
    path('editar/<int:codigo>/', views.v_learning_objectives_edit, name='edit_objetivos'),
    path('delete/<int:codigo>/', views.v_learning_objectives_delete, name='delete_objetivos'),
    path('assessments', views.list_assessment, name='assessment'),
    path('assessments/new', views.new_assessment, name='new_assessment'),
]