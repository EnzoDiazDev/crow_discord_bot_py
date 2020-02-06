async def say(context, *args):

    message_to_print = '...'

    if (len(args)>0):
        message_to_print = ' '.join(args)

    await context.send(message_to_print)

    if(context.guild != None):
        await context.message.delete()
