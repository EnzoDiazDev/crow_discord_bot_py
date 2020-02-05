# Imports
from discord.ext import commands
from events.on_ready import on_ready
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
MODULES_PATH = os.path.join(os.path.dirname(__file__),'commandes','')
FUNCTIONS = import_modules_from_path(MODULES_PATH)

# Variables

# Commands
for function in FUNCTIONS:
    BOT.command()(function)

# Events
BOT.event(on_ready)
