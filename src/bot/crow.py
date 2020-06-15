# Imports
from discord.ext import commands
import os
import sys
import glob
import importlib
from bot.Bot import Bot

# Functions
# def import_modules_from_path(modules_path):
#     functions_list = []

#     sys.path.append(modules_path)
#     modules_files = glob.glob(modules_path+"*.py")

#     for module_file in modules_files:
#         module_name,file_extension = os.path.splitext(os.path.split(module_file)[-1])
#         if module_name.startswith("_"): continue
#         module = importlib.import_module(module_name)
        
#         for y in [getattr(module, x) for x in dir(module)]:
#             if callable(y):
#                 function_name = y.__name__
#                 globals()[function_name] = getattr(module, function_name)

#                 functions_list.append(getattr(module, function_name))

#     return functions_list

# Constants
# LOCALISATION_PATH = os.path.join(os.path.dirname(__file__), "..", 'localisation', '')

# COMMANDES_PATH = os.path.join(os.path.dirname(__file__), "..", 'commandes', '')
# COMMANDES = import_modules_from_path(COMMANDES_PATH)

# DM_COMMANDES_PATH = os.path.join(os.path.dirname(__file__), "..", 'dm_commandes', '')
# DM_COMMANDES = import_modules_from_path(DM_COMMANDES_PATH)

CROW = Bot(command_prefix="!")

# Commands
# for commande in COMMANDES:
#     CROW.command()(commande)

# for dm_commande in DM_COMMANDES:
#     CROW.command()(commands.dm_only()(dm_commande))

# Events
@CROW.event
async def on_ready():
    print('Beepboop o0/')
