from botdata import *
from message_builder import MessageForm, Messager
from sugar import *
import os

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return

        m = Messager(client,message.channel)
        form = MessageForm("", message.channel.id)
        text = none(call(message.content, form),"")
        if text != "": await m(text)
    except Exception as e:
        await message.channel.send(e.__str__())


client.run(os.environ["DISCORD_API_KEY"])
