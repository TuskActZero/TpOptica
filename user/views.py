from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import PacienteForm
from .models import Paciente
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
    return render(request, "secretaria.html",{'form':form})



def ventas(request):
    return render(request, "ventas.html")

def ProfesionalMedico(request):
    return render(request, "medico.html")

def taller(request):
    return render(request, "taller.html")


