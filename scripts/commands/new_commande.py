# This function crate a new module in the commandes folder.
# To use, run the script `pipenv run new_commande`, insert the name command and go to `src/commandes`.
# You find the new file called `_{name}.py`, with underscore to be ignored. 

from os import path

def writefile(name, dm):
    """write a file with passed name"""
    # MODEL is the module model
    MODEL = f"""# import discord

async def {name}(context):
    pass
"""

    # FILENAME is the module filename
    FILENAME = f"_{name}.py"

    # MODULE_PATH is the path of the file
    MODULE_PATH = "./src/commandes"
    if dm: MODULE_PATH = "./src/dm_commandes"
    
    file = open(path.join(MODULE_PATH, FILENAME), "x")
    file.write(MODEL)
    file.close()

    print(f'\nEl commande "{name}" ha sido creado en {MODULE_PATH}/{FILENAME}')

while True: 
    print("\n> Por favor, ingresa el nombre del commande")
    name = input()
    if not name: continue

    print("\n> ¿Es un dm commande? [y]/[N]")
    dm = False
    is_dm = input()
    if is_dm in ["y", "Y", "yes", "si", "YES", "SI"]: dm = True
    
    writefile(name, dm)
    break
