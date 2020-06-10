Repositorio para el bot Crow, gamemaster del juego Otherworld para Discord.

# ‏![](https://cdn.discordapp.com/attachments/406236748289409026/720408898380627978/mini.png) Otherworld

Otherworld es un juego MMO tipo roguelike y coopetitivo, basado en texto y comandos.</br>

`enlaces...`

El juego se encuentra disponible en la plataforma Discord, en un servidor exclusivo, administrado por el bot Crow. </br>

Como gamemaster, Crow deberá encargarse de asegurar el correcto funcionamiento del juego. Será responsable de crear el ambiente y ofrecer las herramientas de interacción a los usuarios. </br>

Lee la lógica del juego en [/src/game/GAME.md](https://github.com/zero-files/crow_discord_bot/tree/master/src/game/GAME.md)

## Getting started

Se da por hecho que tienes Python 3 y Git.

Instala el entorno virtual [pipenv](https://pypi.org/project/pipenv/) como superusuario (sudo) o administrador </br>
`sudo` `pip3 install pipenv`

Clona el repositorio. </br>
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
4
Crea una variable llamada `BOTKEY` y asignale la clave de tu bot de Discord.</br>
Crea una variable llamada `APIKEY`, y asignale una [clave tier 3](https://github.com/zero-files/otherworld_api) (lectura y escritura)</br>

Inicia el bot (recuerda estar con el entorno virtual activado) </br>
`python3 src/main.py`
</br>

### Contribuir 

Para empezar </br>
Lee el [CODE_OF_CONDUCT.md](https://github.com/zero-files/crow_discord_bot/blob/master/CODE_OF_CONDUCT.md)</br>
Lee el [CONTRIBUTING.md](https://github.com/zero-files/crow_discord_bot/blob/master/CONTRIBUTING.md)</br>
Lee los [issues](https://github.com/zero-files/crow_discord_bot/issues)</br>

Es importante encontrarse en el entorno virtual de pipenv antes de encender el bot.</br>
Accedes al entorno desde tu terminal posicionandote en tu proyecto e ingresando</br>
`pipenv shell`

No olvides instalar módulos mediante `pipenv install MODULENAME`, ya que que de ésta manera pipenv podrá gestionar el modulo correctamente. 

Para iniciar el bot, debes, con el entorno virtual activado, ejecutar el comando </br>
`python3 src/main.py`

También puedes hacer uso de los scripts de pipenv </br>
`pipenv run dev`</br>

Puedes salir del entorno virtual con el comando</br>
`exit`

#### Resumen

Elije o crea un issue.</br>
La gran mayoría de los issues deben abarcar una única función, en éste se especificará el nombre y la ubicación de dicha función. 

Gracias a que las funciones no deben tener efectos colaterales, podrás realizar testing de manera sencilla y realizar cambios en el algoritmo sin preocuparte por la integridad de todo el proyecto. 

Una vez que la función realice el trabajo planteado en el issue, crea un pull request y espera una respuesta.</br>
Desde este momento, considera tomar cierto compromiso o responsabilidad sobre tu aporte. De esta manera podrás deshacer, hacer o rehacer según sea o consideres necesario, además de contestar las dudas en torno a tu trabajo y leer las opiniones de otros programadores.

Siguiendo el código de conducta, ningún issue, commit, pull request o comentario estará mal visto. Todos los aportes serán revisados. 

Ante cualquier duda, únete a la discusión en [Discord](https://discord.gg/w7us8z2).

## Estructura del proyecto 

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
│   ├── bot.py
│   └── main.py
│
├── tools/
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
En la carpeta `dm_commandes` se colocan todos los comandos propios de la mensajería privada. </br>
Para ignorar un módulo (un comando), se añade `_` al inicio del nombre del archivo. Así, éste no está importado automáticamente.</br>
Para crear comandos automáticamente mediante una plantilla´, usa el script `pipenv run new_commande`, luego escribe el nombre del comando y ve a `src/commandes`.

En la carpeta `localisation` se encontrarán todos los archivos de localización.

En la carpeta `database` se encontrarán todos los archivos necesarios para conectarse con la API. 

En la carpeta `game` se encontrarán todos los archivos necesarios para el funcionamiento del juego, independiente de Discord. </br>
Para conocer la estructura del juego y más, lee [/src/game/GAME.md](https://github.com/zero-files/crow_discord_bot/tree/master/src/game/GAME.md)

En la carpeta `tools` se encuentran algunas herramientas y scripts para facilitar el desarrollo y deploys.

El archivo `.env` contiene las siguientes variables de entorno:</br>
_* Este archivo debe ser creado manualmente por el dev._

  * BOTKEY *el token de tu bot*
  * APIKEY *el JWT de la API del juego*
  * SIMON *tu id de discord (opcional)*

El archivo `settings.py` contiene la configuración de dotenv. 

El archivo `Pipfile` contiene la configuración del proyecto. Sus dependencias, scripts, etc. </br>
Este archivo es generado y administrado automáticamente por el entorno virtual pipenv. 

## License
This project is licensed under the terms of the MIT license.

---
`Un proyecto de Zero Files`
