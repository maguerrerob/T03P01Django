from django.urls import path, re_path
from .import views

urlpatterns = [
    path("", views.vista_gestion_de_tareas, name="vista_gestion_de_tareas"),
    path("proyectos", views.listar_proyectos, name="listar_proyectos"),
    path("tareas_asociadas_proyectos", views.tareas_proyectos, name="tareas_proyectos"),
    path("usuarios_con_tareas", views.usuarios_asignados_tareas, name="usuarios_asignados_tareas"),
    path("tareas_con_observaciones/<str:obse>", views.tareas_con_observacion, name="tareas_con_observacion"),
    path("tareas_creadas_2anyos/<int:anyo1>/<int:anyo2>", views.tareas_creadas_2anyos, name="tareas_creadas_2anyos"),
    path("ultimo_usuario", views.ultimo_usuario_comentario, name="ultimo_usuario_comentario"),
    path("comentarios_usuarios_empezar/<str:word>/<int:year>", views.comentario_tarea, name="comentario_tarea"),
    path("todas_etiquetas_tareas_proyectos", views.todas_etiquetas_proyecto, name="todas_etiquetas_proyecto"),
]