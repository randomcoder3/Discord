import discord
import os
import keep_alive
from discord.ext import commands
client = commands.Bot( command_prefix='!')
@client.event
async def on_ready():
    print('bot is ready'.format(client))
@client.command()
async def hey(ctx):
    await ctx.send("Hello") 
@client.command() 
async def hi(ctx):
  await ctx.send("Hey")
@client.command()
async def hello (ctx):
   await ctx.send("Hi wassup")
@client.command()
async def introduce(ctx):
   await ctx.send("Hi, I am RKS a bot by Aryaman")
@client.command()
async def gm(ctx):
   await ctx.send("good morning,have a great day")
@client.command()
async def GM(ctx):
   await ctx.send("good morning, have a great day")
@client.command(aliases=['c'])
async def clear(ctx,amount=2):
   await ctx.purge(limit=amount)
@client.command()
async def wassup(ctx):
   await ctx.send("I am Bored, what about you?")
@client.command()
async def Wassup(ctx):
   await ctx.send("I am Bored, what about you?")
@client.command(aliases = ["Good Morning"])
async def good_morning(ctx):
  await ctx.send("Good Morning")
@client.command() 
async def bored(ctx):
   await ctx.send("Here are somethings you can do https://www.arkadium.com/free-online-games/ or listen to some songs? https://www.spotify.com/in/ or maybe some videos https://www.youtube.com/")

@client.command()
async def gn(ctx):
   await ctx.send ("Good night, Have sweet dreams ")
@client.command()
async def games(ctx):
   await ctx.send("https://www.arkadium.com/free-online-games/")
@client.command()
async def songs(ctx):
   await ctx.send("https://www.spotify.com/in/")
@client.command()
async def football(ctx):
   await ctx.send("https://www.espn.in/football/scoreboard")

@client.command()
async def music(ctx):
   await ctx.send("https://www.spotify.com/in/")

@client.command()
async def talk(ctx):
   await ctx.send("Hi i am RKS, i would love to talk to you..so what do you want to talk about")

@client.command()
async def life(ctx):
   await ctx.send("Ok..how is life going? You happy or sad?")

@client.command()
async def news(ctx):
   await ctx.send("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

@client.command()
async def happy(ctx): 
   await ctx.send("Wow, nice to know..i am happy that you are enjoying life")

@client.command()
async def weather(ctx):
    await  ctx.send("https://www.accuweather.com/")

@client.command()
async def videos(ctx):
   await ctx.send("https://www.youtube.com/")

@client.command()
async def game(ctx):
   await ctx.send("Among us (Mobile & PC/Laptop),Valorant(PC/laptop),Call of duty (Mobile/laptop),Grand Theft Auto (Laptop),Getting over it (Laptop)")

@client.command()
async def Music(ctx):
   await ctx.send("https://www.youtube.com/watch?v=7SrJb-jdQao")

@client.command()
async def soothing(ctx):
   await ctx.send("https://www.youtube.com/watch?v=gguPx2BwqQA")

@client.command()
async def party(ctx):
   await ctx.send("https://www.youtube.com/watch?v=Z0kuMR9nW0E")

@client.command()
async def english(ctx):
    await ctx.send("https://www.youtube.com/watch?v=dXLLzpZO_YA")

@client.command()
async def gaming(ctx):
   await ctx.send("https://www.youtube.com/watch?v=vAiScGnRfP8")
  

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))