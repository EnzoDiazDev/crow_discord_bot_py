# Imports
from discord.ext import commands

# Initial functions

# Initial constants
BOT = commands.Bot(command_prefix="!")

# Initial variables

# Commands
@BOT.command()
async def ping(message):
    await message.send("pong!")

# Events
@BOT.event
async def on_ready():
    print('Beepboop o0/')

