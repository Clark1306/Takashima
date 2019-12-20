import discord
import os
from discord.ext import commands
#from discord.ext.commands import Bot
#import asyncio
#import random
#import time
#import typing

bot = commands.Bot(command_prefix="c!")
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="with time and space"))
    print("System Online : Ready for uses")

@bot.command()
async def load(ctx, extension):
    try:
        bot.load_extension(f'cogs.{extension}')
        await bot.say('{} Loaded!'.format(extension))
    except Exception as error:
        print("{} Can't be loaded [{}]".format(extension, error))

@bot.command()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        await bot.say('{} Unloaded!'.format(extension))
    except Exception as error:
        print("{} Can't be unloaded [{}]".format(extension, error))

@bot.command()
async def reload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await bot.say('{} Reloaded!'.format(extension))
    except Exception as error:
        print("{} Can't be reloaded [{}]".format(extension, error))

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')
             

bot.run(os.environ['BOT_TOKEN'])

