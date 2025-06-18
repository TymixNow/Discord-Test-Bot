# This example requires the 'message_content' intent.

from command import LeafCommander
from replacer import Replacer
import os

uwuifier = Replacer({"l": "w", "r": "w", "uwu": "UwU", "owo": "OwO", ":)": ":3", ":D": ":3c", "=)": ">:3", "=D": ">:3c", "xd": "X3"})

game = LeafCommander({"!errorTest":(lambda word: 0/0)}, default=(lambda word: uwuifier(word)))

interaction = LeafCommander({"$": game})


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

        text_cond = interaction(message.content)
        text : str = ""
        if text_cond is not None: text = text_cond
        if text != "": await message.channel.send(text)
    except Exception as e:
        await message.channel.send(e)


client.run(os.environ["DISCORD_API_KEY"])
