from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.http import HttpResponse
from .utils import calc_level
from .forms import Evaluate

# Create your views here.
def index(request):
    '''
    Main page of the framework, shows a form to register
    '''
    return render(request, 'framework/index.html')

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
    return render(request, 'framework/register.html')

def login(request):
    '''
    Manage the intent of authentication of a user
    '''
    username = request.POST['username']
    password = request.POST['password']
    #TODO: Make login here
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_django(request, user)
        form = Evaluate()
        return render(request, 'framework/evaluar.html', {"form": form})

    