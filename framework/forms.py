from django import forms
from framework.models import Learning_Objectives
from framework.choices import *

class Evaluate(forms.Form):
    '''
    Form for the constants
    '''
    constant_r = forms.IntegerField(label="Total de roles", required=True)
    constant_m = forms.IntegerField(label="Total de materiales", required=True)
    constant_s = forms.IntegerField(label="Total de pasos", required=True)
    grade = forms.ChoiceField(label="Evidencia de incorporación",
     required=True, choices=((1,"Null"), (2,"Medium"), (3,"Significant"), (4,"High"), (5,"Very High") ))

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

class Learning_ObjectivesForm(forms.ModelForm):
    class Meta:
        model = Learning_Objectives

        fields = [
            'id',
            'objective',
            'principle',
            'grade',
            'evidence',
            'wid',
        ]

        labels = {
            'id' : 'Código',
            'objective': 'Objetivo',
            'principle': 'Principio',
            'grade': 'Grado',
            'evidence': 'Evidencia',
            'wid' : 'Wid'
        }
        widgets = {
            'id' : forms.NumberInput(attrs={'class':'form-control'}),
            'objective': forms.TextInput(attrs={'class':'form-control'}),
            'principle': forms.Select(choices = PRINCIPLE_CHOICES, attrs={'class':'form-control'}),
            'grade' : forms.Select(choices = GRADE_CHOICES, attrs={'class':'form-control'}),
            'evidence': forms.TextInput(attrs={'class':'form-control'}),
            'wid': forms.NumberInput(attrs={'class':'form-control'})
        }