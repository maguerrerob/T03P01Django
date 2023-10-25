from django.shortcuts import render
from .models import Proyecto, Usuario

# Create your views here.

def vista_gestion_de_tareas(request):
    return render(request, "index.html")

def listar_proyectos(request):
    proyectos = Proyecto.objects.select_related("creador").prefetch_related("proyectos_asignados").all()
    return render(request, "proyectos/listaproyectos.html", {"proyectos":proyectos})