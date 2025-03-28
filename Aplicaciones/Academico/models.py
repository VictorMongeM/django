from django.db import models

# Crear modelos para la base de datos
# models.Model es una clase de Django que representa una tabla en la base de datos
# Cada atributo de la clase representa una columna en la tabla

'''
Django usa un ORM (Object Relational Mapping) para interactuar con la base de datos
Nos permite interactuar con la base de datos sin tener que escribir SQL
Mediante la creación de clases en Python que representan tablas en la base de datos
'''

# Modelo de curso
class Curso(models.Model):
    codigo=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField(default=0)

    # Metodo que retorna una representación en cadena del objeto
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.codigo,self.creditos)