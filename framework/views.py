from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import Login, Register, PrincipleForm, NewAssessment, EvidenceForm
from .models import Principle, Assessment, Evidence

# Create your views here.
def index(request):
    '''
    Main page of the framework, shows a form to register for anonymus or evaluation for logged
    '''
    if request.user.is_authenticated:
        # Do something for logged-in users.
        user = request.user.id
        assessments = Assessment.objects.filter(owner=user)
        context = { 'assessments': assessments }
        return render(request, 'framework/assessment_list.html', context)
    else:
        # Do something for anonymous users.
        form = Login()
        return render(request, 'framework/index.html', { 'form': form })

@login_required
def resultados(request, assessment):
    '''
    Show the result of the evaluation
    '''    
    try:
        a = Assessment.objects.get(id=assessment)
        result = a.level()
        return render(request, 'framework/results.html', {'result': result})
    except:
        return render(request, 'framework/results.html')

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
    return redirect('/', { 'form': form})

@login_required
def v_help(request):
    ''''
    App help
    '''
    return render(request,'framework/help.html')

@login_required
def v_learning_objectives(request, assessment):
    '''
    Method add a learning objectives
    '''
    if request.method == 'POST':
        try:
            post_copy = request.POST.copy()
            post_copy.update({'assessment':assessment})
            form = PrincipleForm(post_copy)
            form.save()
            return redirect('/listobj/' + str(assessment))
        except:
            form = PrincipleForm()
            context = {'form': form, 'error': 'Este principio ya está registrado para la estrategia' ,'id' : assessment }
            return render(request,'framework/objetivos_aprendizaje.html', context)    
    else:
        form = PrincipleForm()
        context = {'form': form, 'id' : assessment }
        return render(request,'framework/objetivos_aprendizaje.html', context)

@login_required
def v_learning_objectives_edit(request, codigo):
    '''
    Method edit a learning objectives
    '''
    inst = Principle.objects.get(id=codigo)
    assessment = inst.assessment_id
    if request.method == 'GET':
        form = PrincipleForm(instance=inst)
        return render(request, 'framework/objetivos_aprendizaje.html', {'form': form, 'id' : assessment })
    else:
        form = PrincipleForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
        return redirect('/listobj/' + str(assessment))    

@login_required
def v_learning_objectives_delete(request, codigo):
    '''
    Method delete a learning objectives
    '''
    inst = Principle.objects.get(id=codigo)
    assessment = inst.assessment_id    
    inst.delete()
    return redirect('/listobj/' + str(assessment))

@login_required
def list_objectives(request, assessment):
    '''
    Method list learning objectives
    '''
    listt = Principle.objects.filter(assessment_id=assessment)
    context = {'lista_obj': listt, 'assessment': assessment}
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

@login_required
def evidence_list(request, identifier):
    '''
    List all the evidences for the principle
    '''
    evidences = Evidence.objects.filter(principle=identifier)
    return render(request, 'framework/evidence_list.html', {'list': evidences})

@login_required
def evidence_new(request, identifier):
    '''
    Creates a new evidence for a indicated principle
    '''
    if request.method == 'POST':
        try:
            post_copy = request.POST.copy()
            post_copy.update({'principle': identifier})
            form = EvidenceForm(post_copy)
            form.save()
            return redirect('/evidencias/' + str(identifier))
        except:
            form = EvidenceForm()
            context = {'form': form, 'error': 'Este principio ya está registrado para la estrategia'}
            return render(request,'framework/new_evidence.html', context)  
    else:
        form = EvidenceForm()
        return render(request, 'framework/new_evidence.html', {'form': form})