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
    await bot.change_presence(game=discord.Game(name="with master"))
    print("I'm ready!")

@bot.command(pass_context=True)
async def kick(ctx, target:discord.Member):
        msg=await bot.say("...")
        time.sleep(0.1)
        await bot.delete_message(ctx.message)
        if ctx.message.server.me.server_permissions.kick_members:
            if ctx.message.author.server_permissions.kick_members:
                await bot.edit_message(msg, new_content=".....")
                time.sleep(0.1)
                if target==ctx.message.server.owner:
                    await bot.edit_message(msg, new_content="no.")
                    await bot.delete_message(msg)
                else:
                    if target==ctx.message.server.me:
                        await bot.edit_message(msg, new_content="no.")
                    else:
                        await bot.edit_message(msg, new_content="..")
                        time.sleep(0.1)
                        try:
                            await bot.kick(target)
                            await bot.edit_message(msg, "done.")
                            await bot.delete_message(msg)
                        except Exception:
                            await bot.edit_message(msg, new_content="no.")
                            await bot.delete_message(msg)
    
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

    embed.set_author(name="===================================================")
    embed.add_field(name="Hello, I'm Astral Codex", value="an unofficial bot created by Clark#8056 and  AJ#2121,", inline=False)
    embed.add_field(name="I have moderation and fun commands, some are still being added,", value="there are some errors here and there,", inline=False)
    embed.add_field(name="I'm still being worked on by the developers,", value="but they're trying their best to finish me and add updates,", inline=False)
    embed.add_field(name="That's all for now, have a good day.", value="==================================================", inline=False)
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
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def accept_invite(ctx, link):
    await bot.accept_invite(link)

@bot.command(pass_context=True)
async def leave_server(ctx):
    await bot.leave_server(link)
    
@bot.command(pass_context=True)
async def clear(ctx, amount=999999999999999999999999999999999999999999999999):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await bot.delete_messages(messages)
            
@bot.command(pass_context=True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

bot.run(os.environ['BOT_TOKEN'])
