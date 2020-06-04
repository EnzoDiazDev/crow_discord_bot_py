# Contributing

Antes de contribuir en este repositorio, por favor
 * lee el [README.md](https://github.com/zero-files/crow_discord_bot/blob/master/README.md),
 * lee nuestro [CODE_OF_CONDUCT.md](https://github.com/zero-files/crow_discord_bot/blob/master/CODE_OF_CONDUCT.md),
 * visita nuestros [issues](https://github.com/zero-files/crow_discord_bot/issues),
 * considera formar parte de la discusión en [discord](https://discord.gg/w7us8z2),
 * termina de leer este archivo. 

Crea un issue planteando el problema a resolver y espera una respuesta. <br>
Sé amable en la discusión y permite que los desarrolladores principales se ofrezcan su ayuda para resolver los problemas serios. <br>
Siéntete libre de crear cualquier issue que tengas en mente. Todas las ideas son bienvenidas, pero asegúrate que ésta no haya sido planteada con anterioridad. 

Sé consciente del roadmap de este proyecto y respeta los tiempos de trabajo. 
Recuerda que éste es un equipo internacional. Sé consciente de las diferencias de idioma y de horario. <br>
Como equipo multidisciplinario, planteamos una filosofía y metodología fija para ponernos de acuerdo. 

## Pull Request process 

... 

### Estilo principal 

Se toma de Python su filosofía modular; basada en módulos y paquetes. <br>
Como desafío, nos hemos planteado utilizar un paradigma fuertemente funcional. <br>

Para facilitar esto, definimos una serie de pautas basadas en los estándares actuales.<br>
*Cualquier otro estilo es bienvenido, se recomienda fuertemente seguir estas sencillas pautas para facilitar las contribuciones.*

 * Define las variables y nombres de funciones en `snake_case` minúsculas, excepto en constantes. 
 * Define los tipos de dato siempre que sea posible.
 * Las constantes se escriben en mayúsculas y no deben ser reasignadas bajo ningún concepto. 
 * Orientado a funciones. Escribe el código en funciones independientes, de principalmente puras y sin efectos colaterales. Investiga más sobre la programación funcional para entender estos conceptos.
 * Colócale nombres descriptivos a las funciones. Asegúrate que éstas o hagan exactamente lo que dice su nombre, no importa si suenan ridículos o son muy extensos. Saca provecho de los módulos y paquetes para crear un juego de verbos descriptivos mediante la notación por punto, como por ejemplo `square.create(x, y)` y `circle.create(radius)`.
 * Las funciones no deben hacer más de una cosa, y es lo que su nombre indique. Una función, un resultado.
 * Las funciones no deberían superar las 50 lineas de código aproximadamente. Caso contrario, se entiende que a esa función se le delegan demasiadas tareas.
 * Las funciones no deben recibir más de tres parámetros. Saca provecho de los [rest parameters](https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558#5720) para una  indefinida cantidad de parámetros. Caso contrario, se entiende que a esa función se le delegan demasiadas tareas.
 * Utiliza un paquete llamado `utils.py` para agrupar funciones generales y misceláneas. 
 * Utiliza `"""docstrings"""` advirtiendo que alguna regla se rompe u ocurren efectos secundarios.
 * Utiliza `"""docstrings"""`, aunque sea de forma concreta para que alguien más pueda desarrollar una documentación más clara y completa.
 * Cuando hagas algo complicado o extraño, coloca `#comentaros` explicando el código. 
 * Todos los módulos deben tener un archivo `cheatsheet.md` a modo documentación, tutorial, borrador y todo lo que considere necesario para un perfecto desarrollo del módulo.
   En este archivo se deberán especificar los paquetes, las funciones, la estructura del modulo, la motivación, los conflictos (incluyendo issues), las ideas, etc. 
   [leer más...](#Cheatsheet)
 * Actualiza el `cheatsheet.md`, actualiza la versión, actualiza el `README.md`, actualiza la documentación. No dejes detalles "para después". 
 * Divide tu flujo de trabajo en tareas concretas, y crea un commit cada vez que finalices.  
 * Hazle justicia a los lenguajes de scripting como Python y utiliza los scripts de automatización en `/tools`. 
 * Crea tus propios scripts de automatización de forma totalmente libre y con tu propio estilo, en un único archivo.

*Visita el issue [#9](https://github.com/zero-files/crow_discord_bot/issues/9) para discutir sobre los puntos aquí expuestos.*

### Ramas 

...

### Cheatsheet

El cheatsheet es una modalidad que tomamos para nuestro flujo de trabajo. 

Es un rápido e informal resumen del contenido de un módulo, idealmente basado en una plantilla generada por los scripts del proyecto. 
Su uso es casi obligatorio, pues agiliza la lectura y análisis del código, tanto para el desarrollo como para la adopción de nuevas contribuciones. 
Además, permite desarrollar sin la necesidad de comprender a ciencia cierta el código desarrollado por otros, basta con leer un resumen para poder comenzar a trabajar. 

El cheatsheet contiene
* Descripción del módulo
* Estructura de archivos (paquetes)
* Funciones
* Versión
* Lista de issues
* to-do list
* Scripts de utilidad
* Contribuidores
* Todo lo que necesites
