# Imports
from discord.ext import commands

from events.on_ready import on_ready

from commandes.ping import ping

# Initial functions

# Initial constants
BOT = commands.Bot(command_prefix="!")

# Initial variables

# Commands
BOT.command()(ping)

# Events
BOT.event(on_ready)

