from django import forms
class Evaluate(forms.Form):
    constant_r = forms.IntegerField(label="Ingrese el valor de la constante r", widget=forms.TextInput, required=True)
    constant_m = forms.IntegerField(label="Ingrese el valor de la constante m", widget=forms.TextInput, required=True)
    constant_s = forms.IntegerField(label="Ingrese el valor de la constante s", widget=forms.TextInput, required=True)