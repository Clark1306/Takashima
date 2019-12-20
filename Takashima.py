import discord
from discord.ext import commands
#from discord.ext.commands import Bot

import asyncio
#import random
#import time
#import typing

import os

bot = commands.Bot(command_prefix="c!")
bot.remove_command('help')

extensions = ['Moderation', 'Events']

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="with time and space"))
    print("System Online : Ready for uses")

@bot.command()
async def reload(extension):
    try:
        bot.unload_extension(extension)
        bot.load_extension(extension)
        await bot.say('{} Reloaded!".format(extension))
    except Exception as error:
        print("{} Can't be reloaded [{}]".format(extension, error))

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
     except Exception as error:
            print("{} Can't be reloaded [{}]".format(extension, error))
             

bot.run(os.environ['BOT_TOKEN'])

