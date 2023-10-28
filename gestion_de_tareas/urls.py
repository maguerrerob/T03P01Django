from django.urls import path, re_path
from .import views

urlpatterns = [
    path("", views.vista_gestion_de_tareas, name="vista_gestion_de_tareas"),
    path("proyectos", views.listar_proyectos, name="listar_proyectos"),
    path("tareas_asociadas_proyectos", views.tareas_proyectos, name="tareas_proyectos"),
    path("usuarios_con_tareas", views.usuarios_asignados_tareas, name="usuarios_asignados_tareas"),
    path("tareas_con_observaciones", views.tareas_con_observacion, name="tareas_con_observacion")
]