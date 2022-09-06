from discord.ext import commands

class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	
    @commands.command()
      async def memberCount(self, ctx):
        members=ctx.guild.member_count
        embed1=discord.Embed(title=f"members in {ctx.guild.name}",description=f"This server has {members} members",color=(0xffff00))
        await ctx.send(embed=embed1)

async def setup(client):
	await client.add_cog(Fun(client))
