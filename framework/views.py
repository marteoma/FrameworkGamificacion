from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from .utils import calc_level
from .forms import Evaluate, Login, Register, Learning_ObjectivesForm

# Create your views here.
def index(request):
    '''
    Main page of the framework, shows a form to register for anonymus or evaluation for logged
    '''
    if request.user.is_authenticated:
        # Do something for logged-in users.
        form = Evaluate()
        return render(request, 'framework/evaluar.html', {"form": form})
    else:
        # Do something for anonymous users.
        form = Login()
        return render(request, 'framework/index.html', { 'form': form })

@login_required
def evaluacion(request):
    '''
    Form for detail the constants of a strategy
    '''        
    form = Evaluate()
    return render(request, 'framework/evaluar.html', {"form": form})

def resultados(request):
    '''
    Show the result of the evaluation
    '''
    r = int(request.POST['constant_r'])
    s = int(request.POST['constant_s'])
    m = int(request.POST['constant_m'])
    grade = int(request.POST['grade'])
    
    result = calc_level(r, m, s, grade)
    return render(request, 'framework/results.html', {'result': result, 'total': result*10})

def register(request):
    '''
    Form to create a new user account
    '''
    form = Register()
    return render(request, 'framework/register.html', {'form': form})

def v_login(request):
    '''
    Manage the intent of authentication of a user
    '''
    username = request.POST['username']
    password = request.POST['password']
    #TODO: Make login here
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        form = Evaluate()
        return render(request, 'framework/evaluar.html', {"form": form})
    else:
        form = Login()
        return render(request, 'framework/index.html', 
        { 'error': 'Usuario o contraseña incorrectos', 'form': form})

def v_logout(request):
    '''
    Close the current user session
    '''
    logout(request)
    form = Login()
    return render(request, 'framework/index.html', 
    { 'form': form})

def v_learning_objectives(request):
    if request.method == 'POST':
        form = Learning_ObjectivesForm(request.POST)
    else:
        form = Learning_ObjectivesForm()

    return render(request,'framework/objetivos_aprendizaje.html', {'form': form})
    