import os
from shutil import rmtree

def touch(package:str, module:str, content:str = ""): 
    file = open(os.path.join(f"./src/{package}", module), "x")
    file.write(content)
    file.close()

def createPackage(name:str, attempts:int = 0):
    if attempts > 5: 
        if os.path.exists(f"./src/{name}"):  
            rmtree(f"./src/{name}")
        return print("> Demasiados intentos, vuelve a correr el comando.")
    
    print("> Creando paquete...")
    
    if not os.path.exists(f"./src/{name}"): 
        try:
            os.mkdir(f"./src/{name}")
        except OSError:
            print(f"ERROR: La creación del paquete {name} ha fallado, reintentando...")
            attempts += 1
            return createPackage(name, attempts)
        else: 
            print(f"> La carpeta {name} ha sido creada.")
    else: 
        print(f"> Eliminando el paquete {name}, reintentando...")
        rmtree(f"./src/{name}")
        attempts += 1
        return createPackage(name, attempts)
    
    CHEATSHEET = "cheatsheet.md"
    INIT = "__init__.py"
    UTILS = "utils.py"

    CHEATSHEET_CONTENT = f"""#Test
    """

    try:
        print("> Creando cheatsheet.md...")
        touch(name, CHEATSHEET, CHEATSHEET_CONTENT)

        print("> Creando __init__.py...")
        touch(name, INIT)

        print("> Creando utils.py...")
        touch(name, UTILS)
    except: 
        print("ERROR: Ha ocurrido un error al crear los archivos, reintentando...")
        attempts += 1
        return createPackage(name, attempts)

    print(f"El paquete {name} ha sido creado correctamente")

while True: 
    print("\n> Ingresa el nombre del paquete:")
    name = input()
    if not name: continue

    if os.path.exists(f"./src/{name}"):
        print(f"ERROR: Ya existe una carpeta o archivo con ese nombre.")
        continue

    createPackage(name)
    break
