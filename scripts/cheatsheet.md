# Scripts
Para correr un script: `pipenv run <name>`

Para crear un nuevo script debes crea una nueva carpeta, crea los archivos necesarios y luego comienza a programar todo lo que quieras. <br>
Ve al archivo *Pipfile* y añade el nuevo comando en `[scripts]`, utilizando la siguente sintaxis <br>
`command_name = python3 path/to/script.py` <br>
Por ejemplo: `new_commande = python3 scripts/commands/new_commande.py`

## Crear un nuevo comado
`pipenv run new_commande`
Selecciona el nombre del comando, especifica si es o no un comando para el chat privado. <br>
Ve a *src/commandes* y busca el nuevo archivo creado. <br>
Comienza a programar.

## Crea un nuevo package
`pipenv run new_package`
Selecciona el nombre del package y ve a *src/package_name*.<br>
Comienza a crear los modulos y no olvides actualizar el *cheatsheet.md*
