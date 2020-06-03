Repositorio para el bot Crow, gamemaster del juego Otherworld para Discord.

# Primer uso
Se da por hecho que tienes Python 3. </br>

Instala pipenv como superusuario (sudo) o administrador </br>
`pip3 install pipenv`

Clona el repositorio. Por supuesto, se da por hecho que tienes git.  </br>
`git clone https://github.com/zero-files/crow_discord_bot.git`</br>
`cd crow_discord_bot/`

Una vez dentro del proyecto, inicia el el entorno virtual de pipenv </br>
`pipenv shell`</br>
El entorno virtual se reconoce por llevar el nombre del proyecto al incio de la entrada de tu terminal </br>
`(crow_discord_bot) xxx@user:~/path/to/crow_discord_bot$`

Instala los módulos requeridos por el proyecto  </br>
`pipenv install`

Crea el archivo .env </br>
`touch .env`

Crea una variable llamada `BOTKEY` y asignale la clave de tu bot de Discord.</br>
Crea una variable llamada `APIKEY`, y asignale una clave tier 3 (lectura y escritura)</br>

Inicia el bot (recuerda estar con el entorno virtual activado) </br>
`python3 src/main.py`
</br>

# Estructura del proyecto 
```
project/
├── src/
│   ├── commandes/
│   │   ├── ping.py
│   │   ├── _ignored_command.py
│   │   └── ...
│   │ 
│   ├── dm_commandes/
│   │   ├── private_ping.py
│   │   ├── _ignored_command.py
│   │   └── ...
│   │
│   ├── localisation/ 
│   │   └── ... 
│   │
│   ├── game/ 
│   │   └── ... 
│   │
│   ├── database/ 
│   │   └── ... 
│   │
│   ├── images/ 
│   │   └── ... 
│   │
│   ├── bot.py
│   └── main.py
│
├── tools/
│   ├── new_commande.py
│   └── ...
│    
├── settings.py 
├── .env*
├── Pipfile
├── .gitignore
├── LICENSE
└── README.md
```

El archivo principal es `main.py`</br>
Este archivo setea las variables de entorno e inicia el bot. Iniciará los procesos vitales para el programa. 

El archivo `bot.py` es el bot en cuestión. </br>
En éste se setean comandos, eventos y funcionalidades propias del bot. 

En la carpeta `commandes` se colocan todos los comandos. Cada archivo es un comando compuesto por, sí o sí, una función con el mismo nombre del archivo.</br>
En la carpeta `dm_commandes` se colocan todos los comandos propios de la mensajería privada. Cada archivo es un comando compuesto por, sí o sí, una función con el mismo nombredel archivo. </br>
Para ignorar un módulo (un comando), se añade `_` al inicio del nombre del archivo. Así, éste no está importado automáticamente.</br>
Para crear comandos automáticamente mediante una plantilla´, usa el script `pipenv run new_commande`, luego escribe el nombre del comando y ve a `src/commandes`.

En la carpeta `tools` se encuentran algunas herramientas de desarrollo.

En la carpeta `localisation` se encontrarán todos los archivos de localización. 

En la carpeta `images` se encontrarán todas las imágenes que el bot requiera. 

En la carpeta `database` se encontrarán todos los archivos necesarios para conectarse con la API. 

En la carpeta `game` se encontrarán todos los archivos necesarios para el funcionamiento del juego, independiente de discord. 

El archivo `settings.py` contiene la configuración de dotenv. 

El archivo `.env` contiene las siguientes variables de entorno: BOTKEY.</br>
_* Este archivo debe ser creado manualmente por el dev._

El archivo `Pipfile` contiene la configuraicón del proyecto. Sus dependencias, scripts, etc. </br>
Este archivo es generado y administrado automáticamente por el entorno virtual pipenv. 
</br>

# Ramas
    ...
</br>

# En el desarrollo
Las constantes se escriben en mayúsculas y, por supuesto, no deben ser reasignadas. 
La convención es usar la `NotacionCamello` _(UpperCamelCase)_ para clases, y `minusculas_con_guiones_bajos` para funciones y métodos. 

Los principales archivos que se deben manipular, son los módulos dentro de los paquetes `commandes`, `events`, etc. </br>
Los modulos serán importados y añadidos al bot -_en `bot.py`_- automáticamente.

Es importante encontrarse en el entorno virtual de pipenv antes de encender el bot.</br>
Accedes al entorno desde tu terminal posicionandote en tu proyecto e ingresando</br>
`pipenv shell`

También puedes salir de él con el comando<br>
`exit`

No olvides instalar módulos mediante `pipenv install MODULENAME`, ya que que de ésta manera pipenv podrá gestionar el modulo correctamente. 

Para iniciar el bot, debes, con el entorno virtual activado, ejecutar el comando </br>
`python3 src/main.py`

Para evitar tener que entrar primero al entorno virtual pipenv, y luego ejecutar el comando de encendido, pipenv permite configurar scripts.</br>
Por ello, para iniciar el bot, desde tu terminal debes posicionarte en tu proyecto e ingresar el comando <br>
`pipenv run dev`</br>
Independientemente de si te encuentras con en el entorno virutal activado o no.
