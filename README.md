# backend_api_rest_django_binar10
Proyecto Desarrollado Para Autenticación de Usuarios y  CRUD de un objeto

# Clone
git https://github.com/brayansilveraCOL/backend_api_rest_django_binar10.git

# Ejecutar en Consola

Ejecutar en la raiz del proyecto

- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

# Objetos

* Entity's =  Entidades
* Type Entity's =  Tipo de Entidades EPS, IPS o ARL
* Locations Country = Paises
* Utils = Utilidades Generales EJ: Clases abstract
* Users =  Objeto para manejo de Usuarios

# Funcionalidad

* Type Entity's : CRUD Para Crear tipo de Entidades, Se busca por el uniqueCode
* Entity's : CRUD Para Crear Entidades, Se busca por el uniqueCode
* Locations Country: CRUD Para Paises, Se busca por el uniqueCode
* Utils: Tiene las clases abstractas para otros objetos

* Users: 

# Auth
Realizar Request a la ruta login/ se envian parametors email y password retorna access y refresh token

# Logica de Negocio

* Todo los usuarios pueden crear usuarios
* Solo el usuario Autenticado puede hacer modificaciones a su perfil o a la url de imagen
* solo se puede litar y retornar usuarios si solo si esta autenticado

# Collection POSTMAN

* backend_api_binario.postman_collection Col de postman para pruebas en los endpoints

# Url documentacion postman

https://documenter.getpostman.com/view/10748947/TzXzCcXu


