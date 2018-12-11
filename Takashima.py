import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random

bot = commands.Bot(command_prefix="c!")
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Nya~!"))
    print("I'm ready!")

@bot.command(pass_context = True)
async def ban(member: discord.Member, days: int = 1):
    if "Bot Access" in [role.id for role in message.author.roles]:
        await bot.ban(member, days)
    else:
        await bot.say("Hey! You don't have permission to do that!")

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    
    embed.set_author(name='Help')
    embed.add_field(name='c!say', value='Makes the bot say something!', inline=False)

    await bot.send_message(author, embed=embed)

@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def yn(context):
    possible_responses = [
        'Ehhh, Maybe?',
        'Yes.',
        'No.',
        'No! Why would you ask that?!',
        'No u',
        'Probably, a yes.',
        'Indeed.',
        'True.',
        'Just leave me alone.',
        'Eek! No! Why would you ask that?',
        'Heck no! get away from me!',
        'Uh huh, Maybe..'
        'I call thats a definitely a yes.',
        'Probably?',
        'Can we just talk about something else instead of that?',
        'No! Why would you ask that!?',
    ]
    await bot.say(random.choice(possible_responses) + " " + context.message.author.mention)

@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

bot.run(os.environ['BOT_TOKEN'])
