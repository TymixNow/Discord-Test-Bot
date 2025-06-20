from botdata import *
from message_builder import MessageForm, Messager
from sugar import *
import os

import discord

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True
intents.voice_states = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    jaychan = jay["channel"]
    chan_id : int = jaychan if isinstance(jaychan, int) else 0
    await client.get_partial_messageable(chan_id).send(prolly_uwu(greeter(squeesher("squeeshbot"))))

@client.event
async def on_presence_update(before : discord.Member, after : discord.Member):
    if before.status != discord.Status.online and after.status == discord.Status.online:
        jaychan = jay["channel"]
        chan_id : int = jaychan if isinstance(jaychan, int) else 0
        await client.get_partial_messageable(chan_id).send(prolly_uwu(greeter(squeesher(str_none(after.nick,"", after.name)))))

@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return

        m = Messager(client,message.channel)
        form = MessageForm("", message.channel.id)
        call(message.content, form)
        if form.text != "": await m(form)
    except Exception as e:
        await message.channel.send(typifier(uwuifier(e.__str__())))


client.run(os.environ["DISCORD_API_KEY"])
