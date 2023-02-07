from django.urls import path
from app1.views import *

urlpatterns = [
#------------------------url principales ↓-------------------------
path("inicio/",inicio, name="Inicio"),
path("verProfesores/",ver_profesores, name="Ver_profesores"),
path("verCursos/",ver_cursos, name="Ver_cursos"),
path("verEstudiantes/",ver_estudiantes, name="Ver_estudiantes"),

#------------url para guardar en base de datos ↓-------------------
path("crearestudiantes/",crear_estudiante, name="crearEstudiante"),
path("crearProfesores/",crear_profesores, name="crearProfesores"),
path("crearCursos/",crear_curso, name="crearCursos"),

#-----------------------url para buscar ↓---------------------------
path("buscar_camada/",busquedaCamada, name="buscar_camada"),
path("resultados_Busqueda/", resultadosBusqueda, name="resultados_busqueda"),

#-----------------------CRUD Profesores↓----------------------------
path("leerProfes/",leerProfesores,name="profesleer"),
path("crearCRUDProfes/",crearProfesores,name="profescrear"),
path("eliminarprofes/<profeNombre>",eliminarprofesores,name="profesorEliminar"),
path("editarprofes/<profeNombre>",editarProfesores,name="profesorEditar"),


#-----------------------CRUD Estudiantes↓---------------------------
path("leerEstudiantes/",leerEstudiantes,name="estudiantesLeer"),
path("crearCRUDEstudiantes/",crearEstudiantes,name="estudiantescrear"),
path("eliminiarestudiante/<estudianteNombre>",eliminarestudiante,name="estudianteEliminar"),
path("editarestudiante/<estudianteNombre>",editarestudiante,name="estudianteEditar"),

#-----------------------CRUD Cursos---------------------------
path("leercursos/",leerCursos,name="cursosLeer"),
path("crearCRUDCursos/",crearCursos,name="cursoscrear"),
path("editarCurso/<cursoNombre>",cursoeditar,name="cursoEditar"),
path("eliminarcurso/<cursoNombre>",eliminarCursos,name="cursoEliminar"),
]