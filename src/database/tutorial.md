Tutorial 
Para realizar peticiones, primero se debe leer la documentación para saber qué solicitar. 
Doc: https://zero-files.github.io/otherworld_docs/documentation.html

Por ejemplo, vamos a requerir la info de un jugador.

Selecciona el módulo correspondiente al verbo HTTP que vas a utilizar. 
(Si vas a hacer una petición get, usa el modulo `get.py`)

Comienza creando una corrutina con un nombre descriptivo para tu petición, sin el verbo como prefijo. 
Las corrutinas se definen usando la palabra reservada `async` antes del `def`

`async def player():`

Decide qué parametros necesitas para realizar una peticion exitosa, leyendo la documentacion.
En este caso, el ID del jugador
No olvides definir el tipo del parámetro. 

`async def player(id:str):`

Llama a la función `request()` del modulo utils. 
  Indica el verbo HTTP de tu peticion. 
  Indica la ruta a la que quieres conectarte. 
  Si es necesario, indica el cuerpo de la petición con un Dict
Esta función `request()` también es una corrutina, debes esperar a que acabe de ejecutarse usando `await`
Guarda la respuesta en una variable. 

```
async def player(id:str):
  response = await request("get", f"/game/player/{id})
```

Imprimí por consola la respuesta. 
Todas las respuestas se ven así.
```
{
  error?: string, 
  message: string, 
  data?: dict
}
```
Nota: Hay que actualizar como se ve la respuesta para obtener más información :maldision: 

Añade condicionales antierrores, procesa los datos como sea necesario y retorna la información de interés.

```
async def player(id:str):
  response = await request("get", f"/game/player/{id})
  return response.data.player
```