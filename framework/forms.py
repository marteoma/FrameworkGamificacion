from django import forms
from .models import Learning_Objectives
from .choices import *

class Login(forms.Form):
    '''
    Form for login
    '''
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    
class Register(forms.Form):
    '''
    Form for register a user
    '''
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    email = forms.CharField(label='', required=True, widget=forms.EmailInput(attrs={'placeholder': 'Correo Electrónico'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

class NewAssessment(forms.Form):
    '''
    Form to create a new assessment
    '''
    name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))

class Learning_ObjectivesForm(forms.ModelForm):

    class Meta:
        model = Learning_Objectives

        fields = [
            'id',
            'objective',
            'principle',
            'grade',
            'evidence',
            'assessment'
        ]

        labels = {
            'id' : 'Código',
            'objective': 'Objetivo',
            'principle': 'Principio',
            'grade': 'Grado',
            'evidence': 'Evidencia',
        }
        widgets = {
            'id' : forms.NumberInput(attrs={'class':'form-control'}),
            'objective': forms.TextInput(attrs={'class':'form-control'}),
            'principle': forms.Select(choices=PRINCIPLE_CHOICES, attrs={'class':'form-control'}),
            'grade' : forms.Select(choices=GRADE_CHOICES, attrs={'class':'form-control'}),
            'evidence': forms.TextInput(attrs={'class':'form-control'}),
            'assessment': forms.HiddenInput()
        }