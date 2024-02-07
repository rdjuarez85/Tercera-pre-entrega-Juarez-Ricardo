from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True,)
    
class TecnicoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    
class TrabajoForm(forms.Form):
    dispositivo = forms.CharField(max_length=50, required=True)
    falla = forms.CharField(max_length=50, required=True)
    observaciones = forms.CharField(max_length=50, required=True)
    estado = forms.CharField(max_length=50, required=True)