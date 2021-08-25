import discord
from discord.ext import commands, tasks
class status_cog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@tasks.loop()
	async def ch_pr(self):
		await self.bot.wait_until_ready()
		listboi = 0
		statuses = ['in ' + str(len(bot.guilds)) + ' servers | !help', 'with ' + str(sum((guild.member_count) for guild in self.bot.guilds)) + ' users | !help', 'on Linode | !help', 'at ' + str(round(bot.latency*1000)) + ' ms | !help', '!ferret | !hug | !pfp', 'on Python 3.8.8 | !help']
		while not self.bot.is_closed():
			status = statuses[listboi]
			await self.bot.change_presence(activity=discord.Game(name=status))
			await asyncio.sleep(10)
			listboi += 1
			if listboi >= 5:
				listboi = 0
def setup(bot):
	bot.add_cog(status_cog(bot))