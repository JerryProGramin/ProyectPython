from django.shortcuts import render, redirect
from .forms import MascotaForm, PersonaForm
from .models import Mascota, Persona
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'index.html')

def crud_persona(request):
    personas = Persona.objects.all() 
    return render(request, 'crud_persona.html', {'personas': personas}) 

def crud_mascota(request):
    mascotas = Mascota.objects.all() 
    return render(request, 'crud_mascota.html', {'mascotas': mascotas}) 

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('crud_mascota') 
    else:
        form = MascotaForm()  

    return render(request, 'crear_mascota.html', {'form': form})

def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    mascota.delete() 
    return redirect('crud_mascota') 

def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('crud_mascota')
    else:
        form = MascotaForm(instance=mascota)

    return render(request, 'editar_mascotas.html', {'form': form, 'mascota': mascota})

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('crud_persona') 
    else:
        form = PersonaForm()  

    return render(request, 'crear_persona.html', {'form': form})

def eliminar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    persona.delete() 
    return redirect('crud_persona') 

def editar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('crud_persona')
    else:
        form = PersonaForm(instance=persona)

    return render(request, 'editar_persona.html', {'form': form, 'mascota': persona})
