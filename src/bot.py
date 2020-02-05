# Imports
from discord.ext import commands
import discord
import os
import sys
import glob
import importlib

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

# Constants
BOT = commands.Bot(command_prefix="!")

COMMANDES_PATH = os.path.join(os.path.dirname(__file__), 'commandes', '')
COMMANDES = import_modules_from_path(COMMANDES_PATH)

EVENTS_PATH = os.path.join(os.path.dirname(__file__), 'events', '')
EVENTS = import_modules_from_path(EVENTS_PATH)

# Variables

# Commands
for commande in COMMANDES:
    BOT.command()(commande)

# Events
for event in EVENTS:
    BOT.event(event)
