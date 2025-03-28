"""
Configuración de URL para el proyecto Universidad.

La lista `urlpatterns` enruta las URLs a las vistas. Para más información, consulte:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Agregar una importación:  from my_app import views
    2. Agregar una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases
    1. Agregar una importación:  from other_app.views import Home
    2. Agregar una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluir otra configuración de URLs
    1. Importar la función include(): from django.urls import include, path
    2. Agregar una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Incluimos las urls de la aplicación Academico
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.Academico.urls')),
]
