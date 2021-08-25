import discord
from discord.ext import commands
from typing import Optional
from discord import Embed, Member
from discord.utils import get
from dotenv import load_dotenv
import random
import asyncio
import requests
import datetime
import inspirobot
import os

class commands_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def hug(self, ctx, target: Optional[Member]):
    await ctx.message.delete()
    target = target or ctx.author
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    embed.set_author(name=target.name + ' has been hugged by ' + ctx.author.name + ' UwU',icon_url=str(target.avatar_url))
    await ctx.message.channel.send(embed=embed)
  @commands.command()
  async def pfp(self, ctx, target: Optional[Member]):
    if not target:
      await ctx.message.delete()
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=ctx.author.avatar_url)
      embed.set_footer(text='Hosted by 𝓣𝓲𝓶𝓶𝔂')
      embed.set_author(name='Here\'s your pfp, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      await ctx.channel.send(embed=embed)
    else:
      await ctx.message.delete()
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=target.avatar_url)
      embed.set_footer(text='Hosted by 𝓣𝓲𝓶𝓶𝔂')
      embed.set_author(name='Here\'s ' + target.name + '\'s pfp, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      await ctx.channel.send(embed=embed)
  @commands.command()
  async def quote(self, ctx):
    await ctx.message.delete()
    quote = inspirobot.generate()
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    embed.set_image(url=str(quote))
    embed.set_footer(text='Generated from https://inspirobot.me/')
    embed.set_author(name='Here\'s your quote, ' + ctx.author.name + '!',icon_url='https://inspirobot.me/website/images/inspirobot-dark-green.png')
    await ctx.channel.send(embed=embed)
  @commands.command()
  async def server(self, ctx):
    await ctx.message.delete()
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    datetime = ctx.guild.created_at
    embed.set_author(name=ctx.guild.name)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name='Owner:', value=ctx.guild.owner, inline=False)
    embed.add_field(name='Members:', value=ctx.guild.member_count, inline=False)
    embed.add_field(name='Region:', value=ctx.guild.region, inline=False)
    embed.add_field(name='Creation Date:', value=datetime.strftime(r'%b %d, %Y'), inline=False)
    await ctx.channel.send(embed=embed)
  @commands.command()
  async def rr(self, ctx):
    await ctx.message.delete()
    embed1 = discord.Embed()
    embed1.colour = 0xffb3f7
    embed1.set_author(name=ctx.author.name + ' spins the barrel...', icon_url='https://cdn.stateofthedapps.com/dapps/ruletka/logo_ruletka_6b0b97d3a01d943b29b43c102e0192687008eb7d6d70a5c0606812db9ed24d05_opti.png')
    embed2 = discord.Embed()
    embed2.colour = 0xffb3f7
    bullet = ['Click! ' + ctx.author.name + ' lives!', 'Click! ' + ctx.author.name + ' lives!', 'Click! ' + ctx.author.name + ' lives!', 'Click! ' + ctx.author.name + ' lives!', 'Click! ' + ctx.author.name + ' lives!', 'BANG! ' + ctx.author.name + ' dies!',]
    embed2.set_author(name=random.choice(bullet), icon_url='https://cdn.stateofthedapps.com/dapps/ruletka/logo_ruletka_6b0b97d3a01d943b29b43c102e0192687008eb7d6d70a5c0606812db9ed24d05_opti.png')
    sent = await ctx.channel.send(embed=embed1)
    await asyncio.sleep(4)
    await sent.edit(embed=embed2)
    await asyncio.sleep(7)
    await sent.delete()
  @commands.command()
  async def shoot(self, ctx, target: Optional[Member]):
    embed = discord.Embed()
    embed.colour = 0xff0000
    embed.set_author(name='*BANG!* ' + target.name + ' was shot to death by ' + ctx.author.name + '!', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Crosshairs_Red.svg/1200px-Crosshairs_Red.svg.png')
    await ctx.message.delete()
    await ctx.channel.send(embed=embed)
  @commands.command()
  async def roll(self, ctx):
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    number = ctx.message.content.replace("!-roll ", "")
    try:
      if isinstance(int(number), int):
        embed.set_author(name=ctx.author.name + ' rolled ' + str(random.randint(1,int(number))) + ' on a ' + number + ' sided dice', 
        icon_url='https://static.thenounproject.com/png/763027-200.png')
        await ctx.message.delete()
        await ctx.channel.send(embed=embed)
    except Exception as ValueError:
      errembed = discord.Embed()
      errembed.colour = 0xe2574c
      errembed.set_author(name='\'' + number + '\' is not a rollable number, ' + ctx.author.name + '!', 
      icon_url='https://image.flaticon.com/icons/png/512/179/179386.png')
      await ctx.message.delete()
      await ctx.channel.send(embed=errembed)
  @commands.command()
  async def weather(self, ctx):
    while True:
      try:
        owmkey = os.getenv('OWM_KEY')
        city=ctx.message.content.replace('!-weather ', '')
        georeq=requests.get('http://api.openweathermap.org/geo/1.0/direct?q=' + city + '&limit=5&appid=' + owmkey)
        geocache=georeq.json()
        latitude=geocache[0]['lat']
        longitude=geocache[0]['lon']
        onereq=requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=' + str(latitude) + '&lon=' + str(longitude) + '&units=imperial&exclude=alerts,hourly,minutely,currently&appid=' + owmkey)
        onecache=onereq.json()
        icon_url = 'http://openweathermap.org/img/wn/' + onecache['daily'][2]['weather'][0]['icon'] + '@2x.png'
        embed = discord.Embed()
        embed.colour = 0xffb3f7
        embed.set_author(name='Today\'s Weather Forecast for ' + geocache[0]['name'] + ', ' + geocache[0]['state'])
        embed.set_thumbnail(url=icon_url)
        embed.description = '**Weather:** ' + str(onecache['daily'][2]['weather'][0]['description']) + '\n**Temperature:** ' + str(round(onecache['daily'][0]['temp']['day'])*1) + '°F\n**Humidity:** ' + str(onecache['daily'][0]['humidity']) + '%'
        await ctx.message.delete()
        await ctx.channel.send(embed=embed)
        break
      except IndexError:
        text = str(ctx.message.content.replace("!-weather ", ""))
        errembed = discord.Embed()
        errembed.colour = 0xe2574c
        errembed.set_author(name='\'' + text + '\' is not a valid city, ' + ctx.author.name + '!', icon_url='https://image.flaticon.com/icons/png/512/179/179386.png')
        await ctx.message.delete()
        await ctx.channel.send(embed=errembed)
        break
def setup(bot):
  bot.add_cog(commands_cog(bot))