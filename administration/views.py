from django import forms
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect


class Login(forms.Form):
    """
    Form for login
    """
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))


# Create your views here.
def index(request):
    """
    Main page of the administration, shows a form to register for anonymus or evaluation for logged
    """
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('administration:current')
    else:
        form = Login()
        return render(request, 'administration/index.html',
                      {'error': 'Usuario o contraseña incorrectos', 'form': form})


def current(request):
    groups = request.user.groups.all()
    g = Group.objects.get(name='admin')
    if request.user.is_authenticated and g in list(groups):
        return render(request, 'administration/admin_info.html')
    else:
        form = Login()
        return render(request, 'administration/index.html', {'form': form, 'error': "No tiene permisos para accceder"})
