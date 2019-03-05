from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .utils import calc_level
from .forms import Evaluate

# Create your views here.
def index(request):
    '''
    Main page of the framework, shows a form to register
    '''
    return render(request, 'framework/index.html')

def evaluacion(request):
    '''
    Form for detail the constants of a strategy
    '''
    form = Evaluate()
    return render(request, 'framework/evaluar.html', {"form":form})

def resultados(request):
    '''
    Show the result of the evaluation
    '''
    return render(request, 'framework/results.html', {'result': calc_level()})
    