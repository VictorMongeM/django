# Importar path que nos permitirá definir las rutas de la aplicación
from django.urls import path
from . import views

# Lista de rutas de la aplicación
# urlpatterns es una lista de rutas que Django buscará para redirigir las peticiones
urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso)
]