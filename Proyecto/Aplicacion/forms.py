from django import forms 
from .models import Mascota, Persona

class MascotaForm(forms.ModelForm):
    class Meta:
        model=Mascota
        fields=[
            'nombre',
            'edad',
            'persona'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la mascota'}),
            'edad': forms.NumberInput(attrs={'placeholder': 'Edad de la mascota'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
        }

class PersonaForm(forms.ModelForm):
    class Meta:
        model=Persona
        fields=[
            'nombre',
            'apellidos',
            'edad',
            'telefono'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la persona'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Nombre de la persona'}),
            'edad': forms.NumberInput(attrs={'placeholder': 'Edad de la persona'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Telefono de la persona'}),
        }
        
