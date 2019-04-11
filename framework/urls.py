from django.urls import path
from . import views

app_name = 'framework'
urlpatterns = [
    path('', views.index, name='index'),    
    path('resultados/<int:assessment>', views.resultados, name='resultados'),
    path('registrar', views.register, name='register'),
    path('login', views.v_login, name='login'),
    path('help', views.v_help, name='help'),
    path('logout', views.v_logout, name='logout'),
    path('objetivos/<int:assessment>', views.v_learning_objectives, name='objetivos'),
    path('listobj/<int:assessment>', views.list_objectives, name='list_objetivos'),
    path('edit_objetivos/<int:codigo>/', views.v_learning_objectives_edit, name='edit_objetivos'),
    path('delete_objetivos/<int:codigo>/', views.v_learning_objectives_delete, name='delete_objetivos'),
    path('assessments', views.list_assessment, name='assessment'),
    path('assessments/new', views.new_assessment, name='new_assessment'),
    path('evidencias/<int:identifier>', views.evidence_list, name='evidencias'),
    path('evidencias_new/<int:identifier>', views.evidence_new, name='new_evidence'),
    
]