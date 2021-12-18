from asyncio.windows_events import NULL
import discord
import os
import random
from discord import mentions

from discord.abc import GuildChannel

client = discord.Client()

freedomDict = dict()
prevAuthor = None

def GetRand(lowerBound, upperBound):
    rand = random.randint(lowerBound, upperBound - 1) # I am lead to believe that randint's upper bound is inclusive
    return rand

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global freedomDict
    global prevAuthor

    username = str(message.author).split('#')[0]
    userMessage = str(message.content)
    channel = str(message.channel.name)

    print(f'{username}: {userMessage} ({channel})')

    if message.author == client.user:
        return

    if message.author.bot:
        return

    if message.author not in freedomDict:
        freedomDict[message.author] = 0

    if userMessage.lower() == 'shut the fuck up a2':
        if (prevAuthor != None):
            randNum = GetRand(0, 100)
            freedomDict[prevAuthor] = randNum + 1
            if (randNum == 0):
                await message.channel.send(f'Cope, seethe, mald')
            elif (randNum == 1):
                await message.channel.send(f'Ok {prevAuthor.mention}, I will shut up for {randNum} message')
            else:
                await message.channel.send(f'Ok {prevAuthor.mention}, I will shut up for {randNum} messages')

    if freedomDict[message.author] <= 0:
        await message.channel.send('Ratio')

    prevAuthor = message.author

    freedomDict[message.author] -= 1

client.run(os.getenv('TOKEN'))