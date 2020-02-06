async def greet(context, *args):

    name = ['']

    if(len(args)>0):
        name = args

    message_to_print = context.bot.localised_string('greet', *name)

    await context.send(message_to_print)

    if(context.guild != None):
        await context.message.delete()
