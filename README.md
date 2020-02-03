# dischordes
Basic repo for dischordes

# Uso
Se da por hecho que tienes python 3. </br>

Instala pipenv como superusuario (sudo) o administrador </br>
`pip3 install pipenv`

Clona el repositorio. Por supuesto, se da por hecho que tienes git.  </br>
`git clone https://github.com/zero-files/dischordes.git`
`cd dischordes/`

Una vez dentro del proyecto, inicia el el entorno virtual de pipenv </br>
`pipenv shell`
El entorno virtual se reconoce por llevar el nombre del proyecto al incio de la entrada de tu terminal </br>
`(dischordes) xxx@user:~/path/to/dischores$`

Instala los módulos requeridos por el proyecto  </br>
`pipenv install`

Crea el archivo .env </br>
`touch .env`

Crea una variable llamada `BOTKEY` y asignale la clave de tu bot de Discord.  </br>

Inicia el bot (recuerda estar con el entorno virtual activado) </br>
`python3 src/main.py`
<br>

# Estructura del proyecto 
</br>
project/</br>
├── src/</br>
│   ├── commandes/</br>
│   │   └── ping.py</br>
│   └── events/</br>
│       └── on_ready.py</br>
├── bot.py</br>
└── main.py</br>

El archivo principal es `main.py`</br>
Este archivo setea las variables de entorno e inicia el bot. Iniciará los procesos vitales para el programa. 

El archivo `bot.py` es el bot en cuestión. </br>
En éste se setean comandos, eventos y funcionalidades propias del bot. 

En la carpeta `commandes` se colocan todos los comandos. Cada archivo es un comando compuesto por, sí o sí, una función con el mismo nombre del archivo. 

En la carpeta `events` se colocan todos los eventos. Cada archivo es un evento compuesto por, sí o sí, una función con el mismo nombre del archivo. 