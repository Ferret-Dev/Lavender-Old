import discord
from discord.ext import commands
import praw
import os
ID = os.getenv('REDDIT_ID')
SECRET = os.getenv('REDDIT_SECRET')
reddit = praw.Reddit(client_id=ID, client_secret=SECRET, user_agent='script:LavenderBot:v2.0 (by u/LavenderTheNom)', check_for_async=False)
class reddit_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def ferret(self, ctx):
    prembed = discord.Embed()
    prembed.colour = 0xffb3f7
    prembed.title = 'Loading Image...'
    prembed.set_footer(text='This process may take some time.')
    await ctx.message.delete()
    sent = await ctx.message.channel.send(embed=prembed)
    while True:
      filetype = ('png', 'jpg', 'jpeg', 'gif')
      post = reddit.subreddit('ferrets').random()
      url = str(post.url)
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=post.url)
      embed.set_footer(text='Images from https://reddit.com/r/ferrets')
      embed.set_author(name='Here you go, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      if url.endswith(filetype):
        await sent.edit(embed=embed)
        if True:
          break
  @commands.command()
  async def fox(self, ctx):
    prembed = discord.Embed()
    prembed.colour = 0xffb3f7
    prembed.title = 'Loading Image...'
    prembed.set_footer(text='This process may take some time.')
    await ctx.message.delete()
    sent = await ctx.message.channel.send(embed=prembed)
    while True:
      filetype = ('png', 'jpg', 'jpeg', 'gif')
      post = reddit.subreddit('foxes').random()
      url = str(post.url)
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=post.url)
      embed.set_footer(text='Images from https://reddit.com/r/foxes')
      embed.set_author(name='Here you go, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      if url.endswith(filetype):
        await sent.edit(embed=embed)
        if True:
          break
  @commands.command()
  async def cat(self, ctx):
    prembed = discord.Embed()
    prembed.colour = 0xffb3f7
    prembed.title = 'Loading Image...'
    prembed.set_footer(text='This process may take some time.')
    await ctx.message.delete()
    sent = await ctx.message.channel.send(embed=prembed)
    while True:
      filetype = ('png', 'jpg', 'jpeg', 'gif')
      post = reddit.subreddit('cats').random()
      url = str(post.url)
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=post.url)
      embed.set_footer(text='Images from https://reddit.com/r/cats')
      embed.set_author(name='Here you go, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      if url.endswith(filetype):
        await sent.edit(embed=embed)
        if True:
          break
  @commands.command()
  async def dog(self, ctx):
    prembed = discord.Embed()
    prembed.colour = 0xffb3f7
    prembed.title = 'Loading Image...'
    prembed.set_footer(text='This process may take some time.')
    await ctx.message.delete()
    sent = await ctx.message.channel.send(embed=prembed)
    while True:
      filetype = ('png', 'jpg', 'jpeg', 'gif')
      post = reddit.subreddit('DogPics').random()
      url = str(post.url)
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=post.url)
      embed.set_footer(text='Images from https://reddit.com/r/DogPics')
      embed.set_author(name='Here you go, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      if url.endswith(filetype):
        await sent.edit(embed=embed)
        if True:
          break
  @commands.command()
  async def collie(self, ctx):
    prembed = discord.Embed()
    prembed.colour = 0xffb3f7
    prembed.title = 'Loading Image...'
    prembed.set_footer(text='This process may take some time.')
    await ctx.message.delete()
    sent = await ctx.message.channel.send(embed=prembed)
    while True:
      filetype = ('png', 'jpg', 'jpeg', 'gif')
      post = reddit.subreddit('BorderCollie').random()
      url = str(post.url)
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=post.url)
      embed.set_footer(text='Images from https://reddit.com/r/BorderCollie')
      embed.set_author(name='Here you go, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      if url.endswith(filetype):
        await sent.edit(embed=embed)
        if True:
          break
  @commands.command()
  async def snep(self, ctx):
    prembed = discord.Embed()
    prembed.colour = 0xffb3f7
    prembed.title = 'Loading Image...'
    prembed.set_footer(text='This process may take some time.')
    await ctx.message.delete()
    sent = await ctx.message.channel.send(embed=prembed)
    while True:
      filetype = ('png', 'jpg', 'jpeg', 'gif')
      post = reddit.subreddit('snowleopards').random()
      url = str(post.url)
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=post.url)
      embed.set_footer(text='Images from https://reddit.com/r/snowleopards')
      embed.set_author(name='Here you go, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      if url.endswith(filetype):
        await sent.edit(embed=embed)
        if True:
          break
  @commands.command()
  async def snek(self, ctx):
    prembed = discord.Embed()
    prembed.colour = 0xffb3f7
    prembed.title = 'Loading Image...'
    prembed.set_footer(text='This process may take some time.')
    await ctx.message.delete()
    sent = await ctx.message.channel.send(embed=prembed)
    while True:
      filetype = ('png', 'jpg', 'jpeg', 'gif')
      post = reddit.subreddit('Sneks').random()
      url = str(post.url)
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=post.url)
      embed.set_footer(text='Images from https://reddit.com/r/Sneks')
      embed.set_author(name='Here you go, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      if url.endswith(filetype):
        await sent.edit(embed=embed)
        if True:
          break
  @commands.command()
  async def horse(self, ctx):
    prembed = discord.Embed()
    prembed.colour = 0xffb3f7
    prembed.title = 'Loading Image...'
    prembed.set_footer(text='This process may take some time.')
    await ctx.message.delete()
    sent = await ctx.message.channel.send(embed=prembed)
    while True:
      filetype = ('png', 'jpg', 'jpeg', 'gif')
      post = reddit.subreddit('Horses').random()
      url = str(post.url)
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=post.url)
      embed.set_footer(text='Images from https://reddit.com/r/Horses')
      embed.set_author(name='Here you go, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      if url.endswith(filetype):
        await sent.edit(embed=embed)
        if True:
          break
  @commands.command()
  async def bleach(self, ctx):
    prembed = discord.Embed()
    prembed.colour = 0xffb3f7
    prembed.title = 'Loading Image...'
    prembed.set_footer(text='This process may take some time.')
    await ctx.message.delete()
    sent = await ctx.message.channel.send(embed=prembed)
    while True:
      filetype = ('png', 'jpg', 'jpeg', 'gif')
      post = reddit.subreddit('Eyebleach').random()
      url = str(post.url)
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_image(url=post.url)
      embed.set_footer(text='Images from https://reddit.com/r/Eyebleach')
      embed.set_author(name='Here\'s your bleach, ' + ctx.author.name + '!',icon_url=str(ctx.author.avatar_url))
      if url.endswith(filetype):
        await sent.edit(embed=embed)
        if True:
          break
def setup(bot):
  bot.add_cog(reddit_cog(bot))