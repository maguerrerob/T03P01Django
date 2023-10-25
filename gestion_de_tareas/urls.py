from django.urls import path, re_path
from .import views

urlpatterns = [
    path("", views.vista_gestion_de_tareas, name="vista_gestion_de_tareas"),
    path("proyectos", views.listar_proyectos, name="listar_proyectos")
]
