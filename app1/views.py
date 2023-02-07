from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
from app1.forms import *

def inicio (request):
    return render (request,"app1/inicio.html")

def ver_profesores (request):
   return render(request,"app1/verProfesores.html")

def ver_estudiantes (request):
    return render (request,"app1/verEstudiantes.html")

def ver_cursos(request):
    return render (request,"app1/verCursos.html")

################# FUNCIONES CREAR ##########################

def crear_estudiante(request):
    if request.method == 'POST':
        miFormulario=estudiantesFormulario(request.POST)
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            estudiante1=estudiantes(nombre=infoDic["nombre"], apellido=infoDic["apellido"],camada=infoDic["camada"])
            estudiante1.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = estudiantesFormulario()
    return render (request, "app1/crearProfesores.html",{"formulario1": miFormulario})
    

def crear_profesores (request):
    if request.method == 'POST':
        miFormulario=profersoresFormulario(request.POST)
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            profesor1=profesores(nombre=infoDic["nombre"], apellido=infoDic["apellido"],camada=infoDic["camada"])
            profesor1.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = profersoresFormulario()
    return render (request, "app1/crearProfesores.html",{"formulario1": miFormulario})

    
def crear_curso(request):
    if request.method == 'POST':
        miFormulario=cursosFormulario(request.POST)
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            curso1=cursos(curso=infoDic["curso"], camada=infoDic["camada"])
            curso1.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = cursosFormulario()
    return render (request, "app1/crearCurso.html",{"formulario1": miFormulario})

################# FUNCIONES BUSCAR ################################

def busquedaCamada(request):
    return render(request, "app1/inicio.html")

def resultadosBusqueda (request):
    if request.GET['camada']:
        camada=request.GET['camada']
        estudiantesFiltro= estudiantes.objects.filter(camada__iexact=camada)
        return render(request,"app1/inicio.html",{"apellido":estudiantesFiltro, "camada":camada})
    else:
        respuesta='No se enviaron datos'
    return HttpResponse (respuesta)

################# CRUD LEER ##############################

def leerProfesores(request):
    profesor=profesores.objects.all()
    contexto={"teachers":profesor}
    return render(request,"app1/leerprofes.html",contexto)

def leerEstudiantes(request):
    estudiante=estudiantes.objects.all()
    contexto={"students":estudiante}
    return render(request,"app1/leerEstudiantes.html",contexto)

def leerCursos(request):
    curso=cursos.objects.all()
    contexto={"courses":curso}
    return render(request,"app1/leercursos.html",contexto)

################ CRUD CREAR ####################################

def crearProfesores(request):
    if request.method == 'POST':
        miFormulario=profersoresFormulario(request.POST)
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            profesor1=profesores(nombre=infoDic["nombre"], apellido=infoDic["apellido"],camada=infoDic["camada"])
            profesor1.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = profersoresFormulario()
    return render (request, "app1/crearProfesores.html",{"formulario1": miFormulario})

def crearEstudiantes(request):
    if request.method == 'POST':
        miFormulario=estudiantesFormulario(request.POST)
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            estudiante1=estudiantes(nombre=infoDic["nombre"], apellido=infoDic["apellido"],camada=infoDic["camada"])
            estudiante1.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = estudiantesFormulario()
    return render (request, "app1/crearestudiante.html",{"formulario1": miFormulario})

def crearCursos(request):
    if request.method == 'POST':
        miFormulario=cursosFormulario(request.POST)
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            curso1=cursos(curso=infoDic["curso"],camada=infoDic["camada"])
            curso1.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = cursosFormulario()
    return render (request, "app1/crearCurso.html",{"formulario1": miFormulario})

    #################### CRUD ELIMINAR ####################################

def eliminarprofesores(request, profeNombre):
    profesor = profesores.objects.get(nombre=profeNombre)
    profesor.delete()
    profe=profesores.objects.all()
    contexto = {"teachers":profe}
    return render(request, "app1/leerprofes.html",contexto)

def eliminarestudiante (request, estudianteNombre):
    alumno = estudiantes.objects.get(nombre=estudianteNombre)
    alumno.delete()
    alumno1=estudiantes.objects.all()
    contexto = {"students":alumno1}
    return render(request, "app1/leerestudiantes.html",contexto)

def eliminarCursos (request, cursoNombre):
    cursada = cursos.objects.get(curso=cursoNombre)
    cursada.delete()
    cursada1=cursos.objects.all()
    contexto = {"courses":cursada1}
    return render(request, "app1/leercursos.html",contexto)
#################### CRUD EDITAR ####################################

def editarProfesores (request, profeNombre):
    profesor=profesores.objects.get(nombre=profeNombre)
    if request.method=="POST":
        miFormulario=profersoresFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.camada=info["camada"]
            profesor.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = profersoresFormulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "camada":profesor.camada})
    return render (request, "app1/profeFormulario.html",{"formulario1": miFormulario, "nombre":profeNombre})

def editarestudiante (request, estudianteNombre):
    alumno = estudiantes.objects.get(nombre=estudianteNombre)
    if request.method=="POST":
        miFormulario=estudiantesFormulario(request.POST)
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data           
            alumno.nombre=infoDic["nombre"]
            alumno.apellido=infoDic["apellido"]
            alumno.camada=infoDic["camada"]
            alumno.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = estudiantesFormulario(initial={"nombre":alumno.nombre, "apellido":alumno.apellido, "camada":alumno.camada})
    return render (request, "app1/estudianteFormulario.html",{"formulario1": miFormulario, "nombre":estudianteNombre})


def cursoeditar (request, cursoNombre):
    cursoedit = cursos.objects.get(curso=cursoNombre)
    if request.method=="POST":
        miFormulario=cursosFormulario(request.POST)
        if miFormulario.is_valid():
            infoDic=miFormulario.cleaned_data
            cursoedit.curso=infoDic["curso"]
            cursoedit.camada=infoDic["camada"]
            cursoedit.save()
            return render(request, "app1/inicio.html")
    else:
        miFormulario = cursosFormulario(initial={"curso":cursos.curso, "camada":cursos.camada})
    return render (request, "app1/cursoFormulario.html",{"formulario1": miFormulario, "curso":cursoNombre})










