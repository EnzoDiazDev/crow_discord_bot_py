async def say(context, *args):

    await context.send(' '.join(args))
    await context.message.delete()
