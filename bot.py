import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

def makeUpper(text, apply):
    if apply:
        return text.upper()
    return text

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('pls argue '):
        endsUpper = message.content[-1:].isupper()

        if message.content.lower().endswith(' no'):
            startsUpper = message.content[-2:-1].isupper()
            await message.channel.send(message.content[10:-2] + makeUpper('y',startsUpper) + makeUpper('es',endsUpper))

        if message.content.lower().endswith(' yes'):
            startsUpper = message.content[-3:-2].isupper()
            await message.channel.send(message.content[10:-3] + makeUpper('n',startsUpper) + makeUpper('o',endsUpper))

    # if message.content == '!stop':
    #     await client.logout()

client.run(token)