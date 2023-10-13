from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(default=timezone.now)
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

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
    #----Relaciones
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    usuarios_asignados = models.ManyToManyField(Usuario, through='Asignacion_de_tarea', related_name="usuarios_asignados")
    etiquetas_asociadas = models.ManyToManyField(Etiqueta)

class Asignacion_de_tarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_finalizacion = models.DateField(default=timezone.now)
    #----Relaciones
    creador = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="usuario_creador")
    tareas = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    proyectos_asignados = models.ManyToManyField(Usuario)

class Asignacion_de_Tareas(models.Model):
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)
    
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    autor = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    comentario_tarea = models.OneToOneField(Tarea, on_delete=models.CASCADE)