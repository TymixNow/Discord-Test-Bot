import discord

class MessageForm:
    def __init__(self, text : str, id : int):
        self.text = text
        self.id = id
    def redirect(self, id):
        self.id = id
        return self
    def rewrite(self, text):
        self.text = text
        return self
    
class Messager:
    def __init__(self, client : discord.Client, source : discord.PartialMessageable):
        self.back = source
        self.client = client
    async def __call__(self, message : MessageForm):
        try:
            await self.client.get_partial_messageable(message.id).send(message.text)
        except discord.HTTPException | discord.Forbidden | discord.NotFound as e:
            await self.back.send(e.__str__())