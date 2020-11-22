from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import PacienteForm , TurnoForm
from .models import Paciente, Turno

# Create your views here.



def base(request):
    
    if request.user.is_authenticated:
        
        return render(request, "user/base.html")
    return redirect('/login')

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return HttpResponseRedirect('/')
    return render (request, "login.html",{'form':form})

def logout(request):

    do_logout(request)

    return HttpResponseRedirect('/')

def gerencia(request):
    return render(request, "gerencia.html")

def secretaria(request):
    form = PacienteForm()
    if request.method == "POST":
        form = PacienteForm(request.POST)
        instancia = form.save(commit=False)
        instancia.save()
        return redirect("/secretaria")
    return render(request, "secretaria.html",{'form':form})

def edit(request, paciente_id):
    instancia = Paciente.objects.get(id=paciente_id)
    form = PacienteForm(instance=instancia)

    if request.method == "POST":
        form = PacienteForm(request.POST, instance=instancia)

        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "editar.html",{'form':form})
    
def turnoView(request):
    context={
        'form':TurnoForm
    }
    if request.method == 'POST':
        formulario = TurnoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje']='Turno guardado'
        else:
            context['form']=formulario
    return render(request, 'turnos.html', context)


def ventas(request):
    return render(request, "ventas.html")

def ProfesionalMedico(request):
    return render(request, "medico.html")

def taller(request):
    return render(request, "taller.html")

def lista(request):
    lista_pacientes = Paciente.objects.all()

    return render(request, "tablapaciente.html",{'lista_pacientes' : lista_pacientes})

