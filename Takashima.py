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
    embed.add_field(name="c!ban", value="Bans a user from the server.", inline=True)
    embed.add_field(name="c!unban", value="Unbans a user that you banned or accidently banned a user.", inline=True)
    embed.add_field(name="c!clear", value="Removes some of the messages.", inline=True)
    embed.add_field(name="===================================================", value="| Other Commands |", inline=False)
    embed.add_field(name="c!about", value="Description of the bot", inline=True)
    embed.set_footer(text="===================================================")
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
    async def ban(self, ctx, user:discord.Member, *, reason:str=None):
        """Bans the specified user from the server"""
        if reason is None:
            reason = bot.get("moderation.no_reason", ctx)
        reason += bot.get("moderation.banned_by", ctx).format(ctx.author)
        try:
            await ctx.bot.ban(user, delete_message_days=0, reason=reason)
        except discord.errors.Forbidden:
            if user.top_role.position == ctx.me.top_role.position:
                await ctx.send(bot.get("moderation.no_ban_highest_role", ctx))
            elif user.top_role.position > ctx.me.top_role.position:
                await ctx.send(bot.get("moderation.no_ban_higher_role", ctx))
            else:
                await ctx.send(bot.get("moderation.no_ban_perms", ctx))
            return
        await ctx.send(bot.get("moderation.ban_success", ctx).format(user))
    
@bot.command(pass_context=True)
@commands.has_role("The Astral Code")
async def special_help(ctx):
            
    author = ctx.message.author
    
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    
    embed.set_author(name='Acces Granted')
    embed.add_field(name="| Special Command |", value="Lets you view the special commands the bot has.", inline=False)
    embed.add_field(name="c!delete_channel", value="Deletes one of the channel.", inline=True)
    embed.set_footer(text="================================================")
    await bot.send_message(author, embed=embed)
    
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
async def clear(ctx, amount=999999999999999999999999999999999999999999999999):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
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
