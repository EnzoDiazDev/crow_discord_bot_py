async def say(context, message):

    await context.send(message)
    await context.message.delete()
