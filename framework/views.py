from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from .utils import calc_level
from .forms import Evaluate, Login, Register, Learning_ObjectivesForm, NewAssessment
from .models import Learning_Objectives, Assessment

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

@login_required
def resultados(request):
    '''
    Show the result of the evaluation
    '''

    grade = int(request.POST['grade'])
    
    result = calc_level(grade)
    return render(request, 'framework/results.html', {'result': result, 'total': result*10})

def register(request):
    '''
    Form to create a new user account
    '''
    if (request.method == 'GET'):
        form = Register()
        return render(request, 'framework/register.html', {'form': form})
    elif (request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()

        #Login the new created user
        user = authenticate(username=username, password=password)
        login(request, user)

        assessments = Assessment.objects.filter(owner=user.id)
        return redirect('/assessments', {'assessments': assessments})

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
        assessments = Assessment.objects.filter(owner=user.id)
        return redirect('/assessments', {'assessments': assessments})
    else:
        form = Login()
        return render(request, 'framework/index.html', 
        { 'error': 'Usuario o contraseña incorrectos', 'form': form})

@login_required
def v_logout(request):
    '''
    Close the current user session
    '''
    logout(request)
    form = Login()
    return render(request, 'framework/index.html', 
    { 'form': form})

@login_required
def v_learning_objectives(request):
    '''
    Method add a learning objectives
    '''
    if request.method == 'POST':
        form = Learning_ObjectivesForm(request.POST)
        form.save()
        return redirect('framework:list_objetivos')
    else:
        form = Learning_ObjectivesForm()

    return render(request,'framework/objetivos_aprendizaje.html', {'form': form})

@login_required
def v_learning_objectives_edit(request, codigo):
    '''
    Method edit a learning objectives
    '''
    inst = Learning_Objectives.objects.get(id=codigo)
    if request.method == 'GET':
        form = Learning_ObjectivesForm(instance=inst)
    else:
        form = Learning_ObjectivesForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
        return redirect('framework:list_objetivos')
    return render(request, 'framework/objetivos_aprendizaje.html', {'form': form})

@login_required
def v_learning_objectives_delete(request, codigo):
    '''
    Method delete a learning objectives
    '''
    inst = Learning_Objectives.objects.get(id=codigo)
    if request.method == 'POST':
        inst.delete()
        return redirect('framework:list_objetivos')
    return render(request,'framework/objetivos_aprendizaje.html', {'form':inst})

@login_required
def list_objectives(request):
    '''
    Method list learning objectives
    '''
    listt = Learning_Objectives.objects.all()
    context = {'lista_obj': listt}
    return render(request, 'framework/lista_obj.html', context)

@login_required
def list_assessment(request):
    '''
    List all the assessment of an user
    '''
    user = request.user.id
    assessments = Assessment.objects.filter(owner=user)
    context = { 'assessments': assessments }
    return render(request, 'framework/assessment_list.html', context)

@login_required
def new_assessment(request):
    '''
    Creates a new assessment linked the current user
    '''
    if request.method == 'POST':
        #The current logged user
        user = request.user

        #Save the new assessment
        user.assessment_set.create(name=request.POST['name'])

        #Gets list of assessment to redirect
        assessments = Assessment.objects.filter(owner=user.id)
        context = { 'assessments': assessments }
        #Redirect to avoid resave when update the page
        return redirect('/assessments', context)
    else:
        form = NewAssessment()
        return render(request, 'framework/assessment_new.html', {'form': form})



    