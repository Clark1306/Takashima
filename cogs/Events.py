import discord
from discord.ext import commands

class Events:
  def _init_(self, bot):
    self.bot + bot

async def on_message(self, message):
        if message.author == self.bot.user:
            return
  
        user = message.author
        msg = message.content
        print(f"{user} said {msg}")
        print("{} said {}".format(user, msg))
    
def setup(bot):
  bot.add_cog{Events(bot)}
