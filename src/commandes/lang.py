async def lang(context, lang=''):

    if(lang!=''):
        context.bot.localisation=lang

    message_to_print = context.bot.localised_string('lang')

    await context.send(message_to_print)

