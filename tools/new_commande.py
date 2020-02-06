# This function crate a new module in the commandes folder.
# To use, run the script `pipenv run new_commande`, insert the name command and go to `src/commandes`.
# You find the new file called `_{name}.py`, with underscore to be ignored. 

from os import path

def writefile(name):
    """write a file with passed name"""
    # MODEL is the module model
    MODEL = f"""# import discord

async def {name}(context):
    pass
"""

    # FILENAME is the module filename
    FILENAME = f"_{name}.py"
    
    file = open(path.join(f"./src/commandes", FILENAME), "w")
    file.write(MODEL)
    file.close()

while True: 
    print("> Por favor, ingresa el nombre del commande")
    name = input()
    if not name: continue
    else: 
        writefile(name)
        break

