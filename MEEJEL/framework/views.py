from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    '''
    Main page of the framework, shows a form to register
    '''
    return render(request, 'framework/index.html')
    