from django.urls import path
from .views import home, crear_mascota, eliminar_mascota, editar_mascota, crear_persona, eliminar_persona, editar_persona, crud_persona, crud_mascota

urlpatterns = [
    path('', home, name='home'),  
    path('mascotas/crud_persona/', crud_persona, name='crud_persona'),
    path('personas/crud_mascota/', crud_mascota, name='crud_mascota'),  
    path('mascotas/crear_mascota/', crear_mascota, name='crear'),   
    path('mascotas/eliminar/<int:mascota_id>/', eliminar_mascota, name='eliminar_mascota'),
    path('mascotas/editar/<int:mascota_id>/', editar_mascota, name='editar_mascota'),
    path('personas/crear_persona/', crear_persona, name='crear_persona'),
    path('personas/eliminar/<int:persona_id>/', eliminar_persona, name='eliminar_persona'),
    path('personas/editar/<int:persona_id>/', editar_persona, name='editar_persona'),
]