import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import time

bot = commands.Bot(command_prefix="c!")
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Nya~!"))
    print("I'm ready!")

@bot.command(pass_context=True, description="Kicks the given member. Please ensure both the bot and the command invoker have the permission 'Kick Members' before running this command.")
async def kick(ctx, target:discord.Member):
    """Boot someone outta the server. See 'c!help' for more."""
    if not str(ctx.message.channel).startswith("Direct Message with "):
        msg=await bot.say("Checking...")
        time.sleep(0.5)
        if ctx.message.server.me.server_permissions.kick_members:
            if ctx.message.author.server_permissions.kick_members:
                await bot.edit_message(msg,new_content="Hmmph, this might take a while.")
                time.sleep(0.5)
                if target==ctx.message.server.owner:
                    await bot.edit_message(msg, new_content="Are you trying to make me kick the owner or yourself? That's just.. I don't even know anymore.")
                else:
                    if target==ctx.message.server.me:
                        await bot.edit_message(msg, new_content="M-Me!? Are you trying to make me kick myself!? How dare you! You heartless bastard!")
                    else:
                        await bot.edit_message(msg, new_content="Found one, i'm checking if i can kick this person..")
                        time.sleep(2)
                        try:
                            await bot.kick(target)
                            await bot.edit_message(msg, "See you later user!")
                        except Exception:
                            await bot.edit_message(msg, new_content="Are you trying to make me kick a higher role than me? That is just rude.")
            else:
                await bot.edit_message(msg, new_content="I don't think you have permission to execute this..")
        else:
            await bot.edit_message(msg, new_content="I don't have the permission to execute this.")
    else:
        await bot.say("This a DM! This command is for servers only.. Try this in a server instead.")

@bot.command(pass_context=True)
async def help(ctx):

    author = ctx.message.author
    
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    
    embed.set_author(name='===================================================')
    embed.add_field(name="| Fun Commands |", value="-", inline=False)
    embed.add_field(name="c!say", value="Makes the bot say something!", inline=True)
    embed.add_field(name="c!8ball", value="Answers your question!", inline=True)
    embed.add_field(name="===================================================", value="| Moderation Commands |", inline=False)
    embed.add_field(name="c!kick", value="Boots a user from your server.", inline=True)
    embed.add_field(name="===================================================", value="| Other Commands |", inline=False)
    embed.add_field(name="c!about", value="No description..", inline=True)
    embed.add_field(name="-------", value="===================================================", inline=False)
    embed.set_footer(text="There would be still more commands to be added, so yeah.")
    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
async def about(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name="==============================================================")
    embed.add_field(name="Hello! I'm Takashima-chan,", value="an unofficial neko bot created by Clark#8056 and  AJ#2121!", inline=False)
    embed.add_field(name="I have moderation and fun commands, some are still being added tho! I'm still being worked on by the developers,", value="there are some errors here and there, but they're trying their best to finish me and add updates!", inline=False)
    embed.add_field(name="That's all for now, have a good day! nyah~", value="==========================================================", inline=False)
    
    await bot.send_message(channel, embed=embed)

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

@bot.command(pass_context=True)
async def delete_channel(ctx, channel: discord.Channel):
    await bot.delete_channel(channel)
    
@bot.command(pass_context = True)
async def clear(ctx, number):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await bot.delete_message(x)
            counter += 1
            await asyncio.sleep(0.1) #1.2 second timer so the deleting process can be even

@bot.command(pass_context=True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

bot.run(os.environ['BOT_TOKEN'])
