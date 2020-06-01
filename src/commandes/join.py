import requests
import database.post

async def join(context):
    res = await database.post.player(context.message.author.id)

    error = res.get('error', None)

    message_to_print = '...'
        
    print (res)

    if(error == None):
        message_to_print = context.bot.localised_string('has_join_game', context.message.author.mention)

    elif(error == 'Player already exists'):
        message_to_print = context.bot.localised_string('has_already_joined_game', context.message.author.mention)

    else:
        message_to_print = context.bot.localised_string('error_joining_game', context.message.author.mention, error)

    await context.send(message_to_print)

    return context.message.author.id
