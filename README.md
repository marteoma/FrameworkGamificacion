El proyecto está en Python usando el Framework __Django__

Para empezar a trabajar se debe hacer lo siguiente

# Instrucciones para Django

## Crear ambiente virtual
1. Instalar virtualenv con el comando pip install virtualenv
2. Crear el ambiente virtual con el comando virtualenv ENV

## Activar ambiente virtual
Windows: ENV\Scripts\activate

Linux: source ENV/bin/activate

Si funcionó al lado de la terminal se mostrará (ENV)
Para salir del ambiente virtual solo hay que escribir deactivate

## Instalar dependencias
Usar el siguiente comando **pip install -r requirements.txt**

Con lo anterior ya se tiene listo el ambiente de trabajo para trabajar.

# Instrucciones para Git

## Actualizar repositorio
git pull

## Mandar cambios
1. git add .
2. git commit -m "< Mensaje sobre el commit >"
3. git push

## Combinar cambios con master
Esto se hace desde github en la opción pull request, se le debe mandar notificación de revisión a todos los miembros.

# Instrucciones base de datos

1. Abrir la terminal de psql, esto ya sea con la que viene al instalar, o desde la terminal si está en el PATH
2. Usar el comando **CREATE DATABASE framework;** No olvidar el _';'_
3. Usar el comando **\c framework** Esto selecciona la base de datos

Con esto ya tienen la base de datos creada y seleccionada para trabajar en la terminal.
La terminal servirá principalmente como fuente de información, todo se hará desde Django.

## Comandos útiles de la terminal PSQL

* **_\\! cls_** Limpia la terminal en Windows
* **_Ctrl + L_** Limpia la terminal en Linux
* **_\d_** Listar tablas de la base de datos
* **_\c database_** Selecciona la base de datos especificada
* **_\l_** Listar todas las bases de datos

Adicionalmente se puede usar cualquier sentencia SQL directamente.
Adicional a esto, si ya tienen el usuario de postgres configurado, deben configurar el usuario
para que el USER sea _postgres_, el PASSWORD sea también _postgres_ y esté en el puerto _5432_
ya que así se aplicó la configuración a Django.

## Migraciones

Para realizar las migraciones, se hace lo siguiente
1. Primero que todo se debe estar situado dentro de MEEJEL en la terminal, al mismo nivel de manage.py
2. Usar el comando **py manage.py migrate**
3. Si todo sale bien, en el terminal de psql, usando la base de datos framework, al buscar las 
tablas (\\d) aparecerá una lista de tablas generadas por Django, en caso contrario, revisar que todo
en la base de datos se cumpla.
