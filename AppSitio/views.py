from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *


# Create your views here.

# ---------------------------------- Home ----------------------------------
def home(request):
    return render(request, "AppSitio/home.html")


# ---------------------------------- Clientes ----------------------------------
def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "AppSitio/clientes.html", contexto)

def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_email = miForm.cleaned_data.get("email")
            cliente = Cliente(nombre = cliente_nombre, apellido = cliente_apellido, email = cliente_email)
            cliente.save()
            return redirect(reverse_lazy('clientes'))
    else:
        miForm = ClienteForm()
    
    contexto = {"form": miForm}
    return render(request, "AppSitio/clienteForm.html", contexto)


# ---------------------------------- Técnicos ----------------------------------
def tecnicos(request):
    contexto = {'tecnicos': Tecnico.objects.all()}
    return render(request, "AppSitio/tecnicos.html", contexto)

def tecnicoForm(request):
    if request.method == "POST":
        miForm = TecnicoForm(request.POST)
        if miForm.is_valid():
            tecnico_nombre = miForm.cleaned_data.get("nombre")
            tecnico_apellido = miForm.cleaned_data.get("apellido")
            tecnico_email = miForm.cleaned_data.get("email")
            tecnico = Tecnico(nombre = tecnico_nombre, apellido = tecnico_apellido, email = tecnico_email)
            tecnico.save()
            return redirect(reverse_lazy('tecnicos'))
    else:
        miForm = TecnicoForm()
    
    contexto = {"form": miForm}
    return render(request, "AppSitio/tecnicoForm.html", contexto)


# ---------------------------------- Trabajos ----------------------------------
def trabajos(request):
    contexto = {'trabajos': Trabajo.objects.all()}
    return render(request, "AppSitio/trabajos.html", contexto)

def trabajoForm(request):
    if request.method == "POST":
        miForm = TrabajoForm(request.POST)
        if miForm.is_valid():
            trabajo_dispositivo = miForm.cleaned_data.get("dispositivo")
            trabajo_falla = miForm.cleaned_data.get("falla")
            trabajo_observaciones = miForm.cleaned_data.get("observaciones")
            trabajo_estado = miForm.cleaned_data.get("estado")
            trabajo = Trabajo(dispositivo = trabajo_dispositivo, falla = trabajo_falla, observaciones = trabajo_observaciones, estado = trabajo_estado)
            trabajo.save()
            return redirect(reverse_lazy('trabajos'))
    else:
        miForm = TrabajoForm()
    
    contexto = {"form": miForm}
    return render(request, "AppSitio/trabajoForm.html", contexto)