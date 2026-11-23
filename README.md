# API REST Hola Mundo - Python y Django

API REST básica desarrollada con Python y Django. Expone un endpoint `GET /api/hola` que responde con un mensaje en formato JSON.

## Requisitos previos

- Python 3.10 o superior (https://www.python.org/downloads/)
- Git (https://git-scm.com/)
- Postman (opcional, para probar la API)

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/JeanPiere898/hola_django.git
cd hola_django
```

2. Crear y activar el entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

En Linux o Mac: `source venv/bin/activate`

3. Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Configuración

No se requiere configuración adicional. La aplicación `api` ya está registrada en `INSTALLED_APPS` dentro de `config/settings.py`.

## Ejecución

```bash
python manage.py runserver
```

El servidor se inicia en `http://127.0.0.1:8000/`. Para detenerlo, presionar `Ctrl + C`.

## Prueba del endpoint

- **Método:** GET
- **URL:** `http://127.0.0.1:8000/api/hola`

Se puede probar desde el navegador o desde Postman. La respuesta esperada tiene código HTTP 200.

## Ejemplo de respuesta JSON

```json
{
  "mensaje": "Hola Mundo",
  "lenguaje": "Python",
  "framework": "Django"
}
```

## Estructura del proyecto

```
hola_django/
├── manage.py
├── requirements.txt
├── config/
│   ├── settings.py
│   └── urls.py
└── api/
    ├── views.py
    └── urls.py
```

## Autor

Jean España - UTEQ, Sistemas de Información