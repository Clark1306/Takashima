import discord
from discord.ext import commands

import asyncio
import os
import random
import time
import typing

bot = commands.Bot(command_prefix="c!")
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="with time and space"))
    print("I'm ready!")

@bot.command(pass_context=True)
async def kick(ctx, target:discord.Member):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        msg=await bot.say("This is a DM chat, it won't work on it unless you do it on a server.")
        time.sleep(0.5)
        await bot.delete_message(ctx.message)
        if ctx.message.server.me.server_permissions.kick_members:
            if ctx.message.author.server_permissions.kick_members:
                await bot.edit_message(msg, new_content="Hold.")
                time.sleep(0.5)
                if target==ctx.message.server.owner:
                    await bot.edit_message(msg, new_content="I can't kick the owner of the server, i can only kick members that doesn't.")
                    await bot.delete_message(msg)
                else:
                    if target==ctx.message.server.me:
                        await bot.edit_message(msg, new_content="Are you seriously kidding me? No, i can't kick myself unless i leave or another bot kicks me.")
                    else:
                        await bot.edit_message(msg, new_content="Wait..")
                        time.sleep(0.5)
                        try:
                            await bot.kick(target)
                            await bot.edit_message(msg, "**{0}** has been kicked!.")
                            await bot.delete_message(msg)
                        except Exception:
                            await bot.edit_message(msg, new_content="I don't have permission to kick this user. Atleast give me adminstrator?")
                            await bot.delete_message(msg)
    
@bot.command(pass_context=True)
async def help(ctx):

    author = ctx.message.author
    
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    
    embed.set_author(name='Fun Commands')
    embed.add_field(name="c!say", value="Makes the bot say something!", inline=False)
    embed.add_field(name="c!8ball", value="Answers your question!", inline=False)
    embed.add_field(name="Moderation Commands", value="‍", inline=False)
    embed.add_field(name="c!kick", value="Boots a user from your server.", inline=False)
    embed.add_field(name="c!ban", value="Bans a user from the server.", inline=False)
    embed.add_field(name="c!unban", value="Unbans a user you banned, even it checks the lists of the unban if you don't unban somebody else yet but left with a blank.", inline=False)
    embed.add_field(name="c!clear", value="Removes messages depends on which number you want to remove.", inline=False)
    embed.add_field(name="c!unmute", value="Makes a user be able to speak again. (Needs a person that have a role named 'Muted' in order to work to remove.)", inline=False)
    embed.add_field(name="c!mute", value="Makes a user unable to speak. (Requires a role named 'Muted' in order to work. Plus, even it won't change the setting of the role so you have to do everything yourself to change that basically.)", inline=False)
    embed.add_field(name="Other Commands", value="‍", inline=False)
    embed.add_field(name="c!about", value="Description of the bot", inline=False)
    embed.set_footer(text="Version 1.0.0 Beta")
    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
async def about(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name="About")
    embed.add_field(name="Hello, I'm Astral Codex", value="an unofficial bot created by Exequiel#8827 and  フォックスAJ#8539,", inline=False)
    embed.add_field(name="I have moderation and fun commands, some are still being added,", value="there are some errors here and there,", inline=False)
    embed.add_field(name="I'm still being worked on by the developers,", value="but they're trying their best to finish me and add updates,", inline=False)
    embed.add_field(name="That's all for now, have a good day.", value="‍", inline=False)
    await bot.send_message(channel, embed=embed)
    
@bot.command()
async def choose(*choices: str):
    """randomly chooses between multiple options"""
    header = 'Bot has randomly chosen...'
    text = random.choice(choices)

    embed = discord.Embed()
    embed.add_field(name=header, value=text, inline=True)
    await bot.say(embed=embed)
    
@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def yn(context):
    possible_responses = [
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            'Do not count on it',
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
    ]
    await bot.say(random.choice(possible_responses) + " " + context.message.author.mention)
    
@bot.command(pass_context=True)
async def delete_channel(ctx, channel: discord.Channel):
    await bot.delete_channel(channel)
    await bot.delete_message(ctx.message)

@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0x00dff)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x00dff)
        await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def slient_kick(ctx, target:discord.Member):
        msg=await bot.say("No...")
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
async def ban(ctx, target:discord.Member):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        msg=await bot.say("This is a DM chat, it won't work on it unless you do it on a server.")
        time.sleep(0.5)
        await bot.delete_message(ctx.message)
        if ctx.message.server.me.server_permissions.kick_members:
            if ctx.message.author.server_permissions.kick_members:
                await bot.edit_message(msg, new_content="Hold.")
                time.sleep(0.5)
                if target==ctx.message.server.owner:
                    await bot.edit_message(msg, new_content="I can't ban the owner of the server, i can only ban members that doesn't.")
                    await bot.delete_message(msg)
                else:
                    if target==ctx.message.server.me:
                        await bot.edit_message(msg, new_content="Are you seriously kidding me? No, i can't ban myself unless i leave or another bot bans me.")
                    else:
                        await bot.edit_message(msg, new_content="Wait..")
                        time.sleep(0.5)
                        try:
                            await bot.ban(target)
                            await bot.edit_message(msg, "**{0}** has been banned!.")
                            await bot.delete_message(msg)
                        except Exception:
                            await bot.edit_message(msg, new_content="I don't have permission to kick this user. Atleast give me adminstrator?")
                            await bot.delete_message(msg)
    
@bot.command(pass_context=True)
@commands.has_role("The Astral Code")
async def special_help(ctx):
    
    author = ctx.message.author
    
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    
    embed.set_author(name='Access Granted')
    embed.add_field(name="Special Command", value="Lets you view the special commands the bot has.", inline=False)
    embed.add_field(name="c!delete_channel", value="Deletes one of the channel.", inline=True)
    embed.set_footer(text="================================================")
    await bot.send_message(author, embed=embed)
    
@bot.command(pass_context=True)
async def embed_test(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    
    embed.set_author(name="Author")
    embed.add_field(name="Field", value="‍" ,inline=False)
    embed.set_footer(text="Footer")
    await bot.send_message(channel, embed=embed)
    
@bot.command(pass_context=True)
async def unban(ctx):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
       ban_list = await bot.get_bans(ctx.message.server)

    # Show banned users
       await bot.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
        await bot.say("Ban list is empty.")
        return
    try:
        await bot.unban(ctx.message.server, ban_list[-1])
        await bot.say("Successfuly unbanned user: `{}`".format(ban_list[-1].name))
    except discord.Forbidden:
        await bot.say("I don't have permission..")
        return
    except discord.HTTPException:
        await bot.say("Unban failed.")
        return

@bot.command(pass_context=True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)


@bot.command()
@commands.is_owner()
async def reload(ctx, cog):
    try:
        bot.unload_extension(f"cogs.{cog}")
        bot.load_extension(f"cogs.{cog}")
        await ctx.send(f"{cog} is reloaded")
    except Exception as e:
        print(f"Error: {cog} can't be loaded:")
        raise e

for cog in os.listdir(".\\cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can't be loaded:")
            raise e

bot.run(os.environ['BOT_TOKEN'])
