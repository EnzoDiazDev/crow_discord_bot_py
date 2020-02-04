# Imports
from discord.ext import commands
from events.on_ready import on_ready
import os
import sys
import glob
import importlib
#from commandes.ping import ping
#from commandes.say import say

modules_path = os.path.join(os.path.dirname(__file__),'commandes','')

def import_modules_from_path(modules_path):

    sys.path.append(modules_path)
    modules_files = glob.glob(modules_path+"*.py")

    for module_file in modules_files:
        module_name,file_extension = os.path.splitext(os.path.split(module_file)[-1])
        module = importlib.import_module(module_name)

        for y in [getattr(module, x) for x in dir(module)]:
            if callable(y):
                function_name = y.__name__
                globals()[function_name] = getattr(module, function_name)

modules_path = os.path.join(os.path.dirname(__file__),'commandes','')
import_modules_from_path(modules_path)

# Initial functions

# Initial constants
BOT = commands.Bot(command_prefix="!")

# Initial variables

# Commands
BOT.command()(ping)
BOT.command()(say)

# Events
BOT.event(on_ready)

