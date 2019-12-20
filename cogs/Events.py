import discord
from discord.ext import commands

class Events:
  def __init__(self, bot):
    self.bot = bot

async def on_message(self, message):
        if message.author == self.bot.user:
            return
  
        user = message.author
        msg = message.content
        print(f"{user} said {msg}")
        print("{} said {}".format(user, msg))

async def on_command_error(self, ctx, error):
  if isinstance(error, commands.CheckFailure)
    
def setup(bot):
  bot.add_cog(Events(bot))
