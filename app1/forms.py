from django import forms

class estudiantesFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    camada=forms.IntegerField()

class profersoresFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    camada=forms.IntegerField()
    
class cursosFormulario(forms.Form):
    curso=forms.CharField()
    camada=forms.IntegerField()
    