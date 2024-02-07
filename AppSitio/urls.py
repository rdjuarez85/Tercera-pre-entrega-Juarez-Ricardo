from django.urls import path
from .views import *


urlpatterns = [
    # ---------------------------------- Home ----------------------------------
    path('', home, name = "home"),
    
    # ---------------------------------- Clientes ----------------------------------
    path('clientes/', clientes, name = "clientes"),
    path('clienteForm/', clienteForm, name = "clienteForm"),
    
    # ---------------------------------- Técnicos ----------------------------------
    path('tecnicos/', tecnicos, name = "tecnicos"),
    path('tecnicoForm/', tecnicoForm, name = "tecnicoForm"),
    
    # ---------------------------------- Trabajos ----------------------------------
    path('trabajos/', trabajos, name = "trabajos"),
    path('trabajoForm/', trabajoForm, name = "trabajoForm"),
]