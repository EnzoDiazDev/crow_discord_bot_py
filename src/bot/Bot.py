from discord.ext import commands

class Bot(commands.Bot):
              # (self, localisation_path='', localisation='es', **args)
    def __init__(self, **args):
        # self._localisation_path = localisation_path
        # self._localisation = localisation
        # self._dico_localisation = self.get_dico_localisation()
        commands.Bot.__init__(self, **args)

    # def get_localisation(self):
    #     return self._localisation

    # def set_localisation(self, localisation):

    #     try:
    #         self._localisation = localisation
    #         self._dico_localisation = self.get_dico_localisation()

    #     except:
    #         self.set_localisation('es')

    # localisation = property(get_localisation, set_localisation)

    # def localised_string(self, string_id, *parameters):
    #     return random.choice(self._dico_localisation.get(string_id, '...')).format(*parameters)

    # def get_dico_localisation(self):
    #     return json.load(open(os.path.join(self._localisation_path,self._localisation+'.json'), encoding='utf-8'))

    async def on_command_error(self, ctx, error):
        if type(error) == commands.errors.PrivateMessageOnly:
            pass
        else:
            return await super().on_command_error(ctx, error)
