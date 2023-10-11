from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(default=timezone.now)
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    ESTADO  = [
        ("PE", "Pendiente"),
        ("PR", "Progreso"),
        ("CO", "Completada")
    ]
    estado = models.CharField(max_length=2, choices=ESTADO)
    completada = models.BooleanField()
    fecha_creacion = models.DateField(default=timezone.now)
    hora_vencimiento = models.TimeField(default=timezone.now)
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_finalizacion = models.DateField(default=timezone.now)
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Asignacion_de_Tareas(models.Model):
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)
    
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)