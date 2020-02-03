# dischordes
Basic repo for dischordes

# Uso
Se da por hecho que tienes python 3. 

Instala pipenv como superusuario (sudo) o administrador
`pip3 install pipenv`

Clona el repositorio. Por supuesto, se da por hecho que tienes git. 
`git clone https://github.com/zero-files/dischordes.git`
`cd dischordes/`

Una vez dentro del proyecto, inicia el el entorno virtual de pipenv
`pipenv shell`
El entorno virtual se reconoce por llevar el nombre del proyecto al incio de la entrada de tu terminal
`(dischordes) xxx@user:~/path/to/dischores$`

Instala los módulos requeridos por el proyecto 
`pipenv install`

Crea el archivo .env
`touch .env`

Crea una variable llamada `BOTKEY` y asignale la clave de tu bot de Discord. 

Inicia el bot (recuerda estar con el entorno virtual activado)
`python3 src/main.py`

# Estructura del proyecto 

