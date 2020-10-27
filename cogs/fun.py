import discord
from discord.ext import commands
class fun(commands.Cog):
    def init(self, client):
        self.client = client
 @commmand.command()
async def good morning(self,ctx):
    await ctx.send("good morning") 
 def setup(client):
  client.add_cog(fun(client))    
