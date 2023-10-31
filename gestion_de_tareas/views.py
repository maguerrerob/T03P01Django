from django.shortcuts import render
from .models import Proyecto, Tarea, Asignacion_de_Tareas, Comentario, Etiqueta
from django.db.models import Q, Prefetch

# Create your views here.

def vista_gestion_de_tareas(request):
    return render(request, "index.html")

def listar_proyectos(request):
    proyectos = Proyecto.objects.select_related("creador").prefetch_related("proyectos_asignados", Prefetch("proyecto_tareas")).all()
    return render(request, "proyectos/listaproyectos.html", {"proyectos":proyectos})

def tareas_proyectos(request):
    QStareas = Tarea.objects.select_related("proyecto").select_related("creador").prefetch_related("usuarios_asignados").prefetch_related("etiquetas_asociadas").all()
    tareas = QStareas.order_by("-fecha_creacion")
    return render(request, "tareas/lista_tareas_asociadas_proyectos.html", {"tareas_asociadas": tareas})

def usuarios_asignados_tareas(request):
    QSasig = Asignacion_de_Tareas.objects.select_related("usuario")
    asig = QSasig.order_by("fecha_asignacion")
    return render(request, "usuarios/usuarios_con_tareas.html", {"asig": asig})

def tareas_con_observacion(request,obse):
    QStareas = Asignacion_de_Tareas.objects.select_related("tarea")
    tareas = QStareas.filter(observaciones__contains=obse)
    return render(request, "tareas/tareas_concretas.html", {"tareass": tareas})

def tareas_creadas_2anyos(request, anyo1, anyo2):
    QStareas = Tarea.objects.filter(fecha_creacion__year__gte = anyo1).filter(fecha_creacion__year__lte = anyo2).filter(estado = "CO")
    return render(request, "tareas/elenco_tareas.html", {"mistareas":QStareas})

def ultimo_usuario_comentario(request, proyecto):
    #QStarea = Tarea.objects.select_related("comentario_tarea").select_related("proyecto").all()
    #tarea = QStarea.order_by()
    #no me sale
    pass

def comentario_tarea(request, word, year):
    QScomentario = Comentario.objects.select_related("comentario_tarea").all()
    comentario = QScomentario.filter(contenido__startswith = word).filter(fecha_comentario__year = year)
    return render(request, "comentarios/comentarios_tarea.html", {"comentarios":comentario})

def todas_etiquetas_proyecto(request):
    QSetiquetas = Tarea.objects.prefetch_related("etiquetas_asociadas").select_related("proyecto").all()
    return render(request, "etiquetas/todas_etiquetas.html", {"etiquetas":QSetiquetas})