import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix="c!")

@bot.event
async def on_ready():
    print("I'm ready!")

@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

bot.run(os.environ['BOT_TOKEN'])
