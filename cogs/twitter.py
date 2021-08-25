import discord
from discord.ext import commands
import tweepy
import os
from dotenv import load_dotenv
C_TOKEN = os.getenv('C_TOKEN')
C_SECRET = os.getenv('C_SECRET')
A_TOKEN = os.getenv('A_TOKEN')
A_SECRET = os.getenv('A_SECRET')
auth = tweepy.OAuthHandler(C_TOKEN, C_SECRET)
auth.set_access_token(A_TOKEN, A_SECRET)
api = tweepy.API(auth)
class twitter_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  @commands.is_owner()
  async def tweet(self, ctx):
    await ctx.message.delete()
    text = ctx.message.content.replace('!-tweet ', '')
    api.update_status(text)
    await ctx.channel.send('Twitter message \'' + text + '\' posted successfully')
def setup(bot):
  bot.add_cog(twitter_cog(bot))