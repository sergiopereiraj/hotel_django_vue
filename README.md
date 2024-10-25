# Proyecto de API de Sorteo

Este es un proyecto de una API construida con Django y Django REST Framework que permite gestionar un sorteo para un concurso de un hotel. Los usuarios pueden registrarse, verificar su correo electrónico y participar en el sorteo.

## Tecnologías Utilizadas

- Django
- Django REST Framework
- MySQL
- Bootstrap (para el frontend)
- Vue.js/Nuxt (para el frontend)

## Requisitos Previos

Asegúrate de tener instalado lo siguiente:

- Python 3.x
- Node.js (si usas Vue.js)
- MySQL

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone <URL del repositorio>
   cd <nombre del proyecto>

2. **Crear un entorno Virtual**

```
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```
3. **Instalar dependencias:**
```
pip install -r requirements.txt
```
4. **Configurar tus variables de entorno**
```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña
DEFAULT_FROM_EMAIL=tu_correo@gmail.com
```
5. **Configurar tu base de dato (django tiene como default sqlite)**

```
python manage.py makemigrations
python manage.py migrate
```

7. **Corre tu proyecto:**

**Back:**
```
python manage.py runserver
```

**front:** 
```

npm run serve
```




