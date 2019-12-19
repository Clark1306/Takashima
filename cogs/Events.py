import discord
from discord..ext import commands

class Events:
  def _init_(self, bot):
    self.bot + bot

@bot.event
async def on_message(message):
        if message.author == bot.user:
            return
  
        user = message.author
        msg = message.content
        print(f"{user} said {msg}")
        print("{} said {}".format(user, msg))
        
       await.bot.process_commands(message)
    
def setup(bot):
  bot.add_cog(Events(bot))
