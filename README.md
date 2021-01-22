# Prueba Grupo Ospedale
Prueba de conocimiento
## CrudUsers
Cruduser es una aplicacion web construida en Django la cual cuenta con las siguientes caracteristicas  
### Caracteristicas

- Login
-  Creacion de usuarios 
- Actualizacion de la informacion de usuarios
- Borrar un usuario

Puede ver el codigo fuente en Github [Aquí](https://github.com/Joldiazch/TestG8)

### Stack de tecnología
#### Backend
- Python
- Django
- Docker

#### Front-end
- Javascript
- Html
- CSS


### Requerimientos

[Ubuntu 16.04](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (Hice uso WSL2 con ubuntu 16.04) 
[Docker](https://docs.docker.com/engine/install/ubuntu/)
[Docker Compose](https://docs.docker.com/compose/install/)
Tambien puede installar [Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

### Modelo Entidad Relación
![](https://i.ibb.co/RQV5zgr/ERD-import-example.png)

### Correr el proyecto
Luego de tener instalado en tu maquina docker y docker compose procedemos a lo siguiente:

Dentro del folder ***TestG8*** ejecutar:

`$ docker-compose up`

Esto levantará dos containers de docker llamados ***testg8_web_1***  y  ***testg8_db_1***  el primero es el servicio encargado de correr la aplicacion de Django mientras el segundo es el encargado de ejecutar una base de datos de Postgresql en la cual se almacena toda la informacion.

### Ejecutar migraciones
Para que El ORM de Django haga su magia y escriba los modelos en la base de datos debemos ejecutar las migraciones, para ello, en una nueva terminal y dentro de la carpeta ***TestG8***  ejecutamos: 

`$ docker exec -it testg8_web_1 python manage.py makemigrations`

y luego

`$ docker exec -it testg8_web_1 python manage.py migrate`

Esto mapeará los modelos y sus relaciones en tablas de nuestra base de datos de postgresSql que está corriendo en un container de Docker

Para acceder a la interfaz en su navegador ingrese ***localhost***  solamente, sin especificar ningun puerto y verá lo siguiente:

![](https://i.ibb.co/NFW9gDF/login-g8.png)

Para ingresar por primera vez, nos dirigimos a la consola y dentro de la carpeta ***TestG8***  ejecutamos en siguiente comanto:

`$ docker exec -it testg8_web_1 python manage.py createsuperuser`

Aparecera en la linea de comandos la siguiente instrucction, insertamos el username con el que haremos login

![](https://i.ibb.co/N2xDp8c/superuser.png)

Con estas credenciales nos dirigimos nuevamnet al ***localhost*** y hacer el respoectivo login.

Luego de hacer el login lo redireccionará a ***http://localhost/users***

![](https://i.ibb.co/1GvT2q6/lista.png)

Donde podrá ver la lista de usuarios creados (Entiendase en el momento usted está logueado como Superuser, por lo tanto su usuario no aparecerá en la lista)

Para registrar usuarios puede hacer uso del boton en la parte superior izquierda

Tambien puede hacer uso de las opciones de editar y eliminar usuarios *Cuando ya haya creado algunos*
