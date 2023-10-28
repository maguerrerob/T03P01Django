from django.shortcuts import render
from .models import Proyecto, Usuario, Tarea, Asignacion_de_Tareas

# Create your views here.

def vista_gestion_de_tareas(request):
    return render(request, "index.html")

def listar_proyectos(request):
    proyectos = Proyecto.objects.select_related("creador").prefetch_related("proyectos_asignados").all()
    return render(request, "proyectos/listaproyectos.html", {"proyectos":proyectos})

def tareas_proyectos(request):
    QStareas = Tarea.objects.select_related("proyecto").select_related("creador").prefetch_related("usuarios_asignados").prefetch_related("etiquetas_asociadas").all()
    tareas = QStareas.order_by("-fecha_creacion")
    return render(request, "tareas/lista_tareas_asociadas_proyectos.html", {"tareas_asociadas": tareas})

def usuarios_asignados_tareas(request):
    QSasig = Asignacion_de_Tareas.objects.select_related("usuario")
    asig = QSasig.order_by("fecha_asignacion")
    return render(request, "usuarios/usuarios_con_tareas.html", {"asig": asig})

def tareas_con_observacion(request, obs):
    QStareas = Asignacion_de_Tareas.objects.prefetch_related("tarea")
    tareas = QStareas.filter(observaciones__contains = obs)
    return render(request, "tareas/tareas_concretas.html", {"tareas": tareas})