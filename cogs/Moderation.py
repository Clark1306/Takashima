import discord
from discord.ext import commands

class Mod:
  def __init__(self, bot):
    self.bot = bot

@commands.command()
@commands.has_permissions(manage_messages=True)
async def clear(self, ctx, amount: int):
    channel = ctx.channel
    await channel.purge(limit=amount+1)
    
    await ctx.send(f"(amount) messages have been deleted")
    await ctx.delete_message(ctx.message)
    
@clear.error
async def clear_error(self, ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.say("You don't have permission to delete.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.say("There's no amount of numbers that i could delete.")
    if isinstance(error, commands.BadArgument):
        await ctx.say("That's not a number.")
        
    raise error

def setup(bot):
  bot.add_cog(Moderation(bot))
