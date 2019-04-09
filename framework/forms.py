from django import forms
from .models import Principle, Evidence
from .choices import PRINCIPLE_CHOICES, GRADE_CHOICES, PRINCIPLES_TYPES_CHOICES

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

class PrincipleForm(forms.ModelForm):

    class Meta:
        model = Principle

        fields = [            
            'principle',
            'grade',
            'justification',
            'assessment',
        ]

        labels = {            
            'principle': 'Principio',
            'grade': 'Grado',
            'justification': 'Justificacion',
        }
        widgets = {            
            'principle': forms.Select(choices=PRINCIPLE_CHOICES, attrs={'class':'form-control'}),
            'grade' : forms.Select(choices=GRADE_CHOICES, attrs={'class':'form-control'}),
            'justification': forms.TextInput(attrs={'class':'form-control'}),
            'assessment': forms.HiddenInput()
        }

class EvidenceForm(forms.ModelForm):

    class Meta:
        model = Evidence

        fields = [            
            'sort',
            'description',   
            'principle',
        ]

        labels = {            
            'sort': 'Tipo',
            'description': 'Descripción',            
        }
        widgets = {            
            'sort': forms.Select(choices=PRINCIPLES_TYPES_CHOICES, attrs={'class':'form-control'}),            
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'principle': forms.HiddenInput()
        }