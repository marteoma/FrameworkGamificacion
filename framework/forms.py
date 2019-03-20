from django import forms
from framework.models import Learning_Objectives

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
    username = forms.CharField(label="Usuario", required=True)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput)    
    
class Learning_ObjectivesForm(forms.ModelForm):
    class Meta:
        model = Learning_Objectives

        fields = [
            'id',
            'objective',
        ]

        labels = {
            'id' : 'Código',
            'objective': 'Objetivo',
        }
        widgets = {
            'id' : forms.TextInput(attrs={'class':'form-control'}),
            'objective': forms.TextInput(attrs={'class':'form-control'})
        }