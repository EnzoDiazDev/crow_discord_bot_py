# Imports
from discord.ext import commands
from events.on_ready import on_ready
import os
import sys
import glob
import importlib
import json
import random

class customBot(commands.Bot):
    def __init__(self, localisation_path='', localisation='es', **args):

        self._localisation_path = localisation_path
        self._localisation = localisation
        self._dico_localisation = self.get_dico_localisation()
        commands.Bot.__init__(self, **args)

    def get_localisation(self):
        return self._localisation

    def set_localisation(self, localisation):

        try:
            self._localisation = localisation
            self._dico_localisation = self.get_dico_localisation()

        except:
            self.set_localisation('es')

    localisation = property(get_localisation, set_localisation)

    def localised_string(self, string_id, *parameters):
        return random.choice(self._dico_localisation.get(string_id, '...')).format(*parameters)

    def get_dico_localisation(self):
        return json.load(open(os.path.join(self._localisation_path,self._localisation+'.json')))

# Functions
def import_modules_from_path(modules_path):
    functions_list = []

    sys.path.append(modules_path)
    modules_files = glob.glob(modules_path+"*.py")

    for module_file in modules_files:
        module_name,file_extension = os.path.splitext(os.path.split(module_file)[-1])
        if module_name.startswith("_"): continue
        module = importlib.import_module(module_name)
        
        for y in [getattr(module, x) for x in dir(module)]:
            if callable(y):
                function_name = y.__name__
                globals()[function_name] = getattr(module, function_name)

                functions_list.append(getattr(module, function_name))

    return functions_list

# Variables


# Constants

LOCALISATION_PATH = os.path.join(os.path.dirname(__file__), 'localisation', '')

COMMANDES_PATH = os.path.join(os.path.dirname(__file__), 'commandes', '')
COMMANDES = import_modules_from_path(COMMANDES_PATH)

DM_COMMANDES_PATH = os.path.join(os.path.dirname(__file__), 'dm_commandes', '')
DM_COMMANDES = import_modules_from_path(DM_COMMANDES_PATH)

BOT = customBot(command_prefix="!", localisation_path=LOCALISATION_PATH, localisation='es')

# Commands
for commande in COMMANDES:
    BOT.command()(commande)

for dm_commande in DM_COMMANDES:
    commands.dm_only()(BOT.command()(dm_commande))

# Events
BOT.event(on_ready)
