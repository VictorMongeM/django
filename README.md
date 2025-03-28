# Ejemplo
Descargar el contenedor:
```bash
docker pull hectorgh24/django:v1
```

En el directorio raíz del repositorio:
```bash
docker run -it --rm -p 80:8000 -v .:/app hectorgh24/django:v1 sh
```

Moverse al directorio /app y ejecutar:
```bash
python manage.py runserver 0.0.0.0:8000
```