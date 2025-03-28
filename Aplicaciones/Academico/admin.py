from django.contrib import admin
# Importar los modelos
from .models import Curso

# Registrar los modelos
admin.site.register(Curso)