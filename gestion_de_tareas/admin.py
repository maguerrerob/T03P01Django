from django.contrib import admin
from .models import Usuario, Tarea, Proyecto, Etiqueta, Asignacion_de_Tareas, Comentario

# Register your models here.

misModelos = [
    Usuario,
    Tarea, 
    Proyecto, 
    Etiqueta, 
    Asignacion_de_Tareas, 
    Comentario
]
admin.site.register(misModelos)