# render es una función que se encarga de renderizar los templates
from django.shortcuts import render, redirect
# Importar el modelo Curso
from .models import Curso

# Crear las vistas de la aplicación
# Las vistas se definen como funciones que reciben un objeto request (una petición) y retornan un objeto response (una respuesta)


# Vista home
def home(request):
    # Guardar en la variable todos los cursos de la base de datos
    cursosListados = Curso.objects.all()

    # Enviar los cursos a la plantilla bajo el nombre "cursos"
    return render(request, "gestionCursos.html", {"cursos": cursosListados})


# Vista registrarCurso
# request es un objeto que contiene toda la información de la petición
def registrarCurso(request):
    # Obtener los datos del formulario
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    creditos = request.POST["numCreditos"]

    # Crear un nuevo curso con los datos recibidos
    # objects.create() es un método que crea un nuevo objeto en la base de datos
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect("/")

# Vista que mandará la plantilla de edición de curso
def edicionCurso(request, codigo):
    # Obtener el curso 
    curso = Curso.objects.get(codigo=codigo)

    # Retornar la plantilla de edición de curso con el curso a editar
    return render(request, "edicionCurso.html", {"curso": curso})


# Vista editar curso
def editarCurso(request):
    # Obtener los datos del formulario
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    creditos = request.POST["numCreditos"]

    # Buscar el curso con el código recibido
    curso = Curso.objects.get(codigo=codigo)
    # Actualizar los datos del curso
    curso.nombre = nombre
    curso.creditos = creditos
    # .save() es un método que guarda los cambios en un objeto de la base de datos
    curso.save()

    return redirect("/")


# Vista eliminar curso
def eliminarCurso(request, codigo):
    # Buscar el curso con el código recibido
    curso = Curso.objects.get(codigo=codigo)

    # Eliminar el curso
    # .delete() es un método que elimina un objeto de la base de datos
    curso.delete()

    return redirect("/")