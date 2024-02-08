from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name = "home"),
    path('nosotros/', nosotros, name = "nosotros"),
    path('contacto/', contacto, name = "contacto"),
    
    # ---------------------------------- Clientes ----------------------------------
    path('clientes/', clientes, name = "clientes"),
    path('clienteForm/', clienteForm, name = "clienteForm"),
    path('buscarClientes/', buscarClientes, name = "buscarClientes"),
    
    # ---------------------------------- Técnicos ----------------------------------
    path('tecnicos/', tecnicos, name = "tecnicos"),
    path('tecnicoForm/', tecnicoForm, name = "tecnicoForm"),
    path('buscarTecnicos/', buscarTecnicos, name = "buscarTecnicos"),
    
    # ---------------------------------- Trabajos ----------------------------------
    path('trabajos/', trabajos, name = "trabajos"),
    path('trabajoForm/', trabajoForm, name = "trabajoForm"),
    path('buscarTrabajos/', buscarTrabajos, name = "buscarTrabajos"),
]