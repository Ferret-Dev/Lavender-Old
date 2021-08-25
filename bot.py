#imports
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
from typing import Optional
from discord import Embed, Member
import inspirobot
import random
import asyncio
import praw
import requests
import datetime

#definitions
bot = commands.Bot(command_prefix='!-')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#reddit
ID = os.getenv('REDDIT_ID')
SECRET = os.getenv('REDDIT_SECRET')
reddit = praw.Reddit(client_id=ID, client_secret=SECRET, user_agent='script:LavenderBot:v2.0 (by u/LavenderTheNom)', check_for_async=False)

#general commands
@bot.command()
async def ping(ctx):
  await ctx.message.delete()
  rounded = round(bot.latency*1000)
  embed = discord.Embed()
  embed.colour = 0xffb3f7
  embed.set_author(name='Lavender is online, ' + ctx.author.name + '! Latency is ' + str(rounded) + 'ms.',icon_url=str(ctx.author.avatar_url))
  await ctx.channel.send(embed=embed)
@bot.command()
async def suggest(ctx):
  await ctx.message.delete()
  embed = discord.Embed()
  embed.colour = 0xffb3f7
  embed.set_author(name= 'Your suggestion was added, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
  await(await ctx.send(embed=embed)).delete(delay=20)
  user = await bot.fetch_user('438111061535621130')
  embed = discord.Embed()
  embed.colour = 0xffb3f7
  embed.set_author(name=ctx.author.name + ' suggested:',icon_url=str(ctx.author.avatar_url))
  embed.description = ctx.message.content.replace("!suggest ", "")
  await user.send(embed=embed)
@bot.command()
@commands.is_owner()
async def cogs(ctx):
  embed = discord.Embed()
  embed.colour = 0xffb3f7
  embed.set_author(name='commands, errors, reddit, twitter')
  await ctx.channel.send(embed=embed)
@bot.command()
@commands.is_owner()
async def re(ctx):
  selcog = ctx.message.content.replace("!-re ", "")
  bot.reload_extension('cogs.' + str(selcog))
  await ctx.channel.send('Reloaded cogs.' + selcog)
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")
bot.run(TOKEN)