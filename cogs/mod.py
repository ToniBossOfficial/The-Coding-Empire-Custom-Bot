from discord.ext import commands

class Mod(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	
	@commands.command()
	async def ban(self, ctx):
		await ctx.send("Not done...")

async def setup(client):
	await client.add_cog(Mod(client))