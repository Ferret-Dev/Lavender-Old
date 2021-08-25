import discord
from discord.ext import commands
class error_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      embed = discord.Embed()
      embed.colour = 0xe2574c
      embed.set_author(name='\'' + ctx.message.content + '\' is not a command, ' + ctx.author.name + '! Use !help for commands.', icon_url='https://image.flaticon.com/icons/png/512/179/179386.png')
      await ctx.message.delete()
      await ctx.channel.send(embed=embed)
  @commands.command()
  async def cogtest(self, ctx):
    await ctx.channel.send('cog loaded. test complete.')
def setup(bot):
  bot.add_cog(error_cog(bot))