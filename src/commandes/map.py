import discord
import json
import requests

async def cmap(context, x1=-10, x2=10, y1=-10, y2=10):

    #guild = context.guild
    #admin_role = discord.utils.get(guild.roles, name="Admin")

    #print discord.Permissions.all()

    #overwrites = {
    #guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, manage_channels=False, create_instant_invite=False, kick_members=False, ban_members=False, administrator=False, manage_guild=False, add_reactions=False, view_audit_log=False, priority_speaker=False, stream=False, send_tts_messages=False, manage_messages=False, embed_links=False, attach_files=False, read_message_history=False, mention_everyone=False, external_emojis=False, use_external_emojis=False, view_guild_insights=False, connect=False, speak=False, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=False, change_nickname=False, manage_nicknames=False, manage_roles=False, manage_permissions=False, manage_webhooks=False, manage_emojis=False),
    #}
    #await context.guild.create_text_channel(name=name, overwrites=overwrites)

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            name = "casilla﹙"+str(x)+"，"+str(y)+"﹚"

            if(not discord.utils.get(context.guild.text_channels, name=name)):
                await context.guild.create_text_channel(name=name)

async def dmap(context, x1=-10, x2=10, y1=-10, y2=10):

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            name = "casilla﹙"+str(x)+"，"+str(y)+"﹚"

            channel = discord.utils.get(context.guild.text_channels, name=name)

            #print("Deleting : "+"("+str(x)+","+str(y)+")"+"\n")

            if(channel != None):
                await channel.delete()


