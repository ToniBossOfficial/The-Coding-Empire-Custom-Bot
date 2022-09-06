from discord.ext import commands

import requests
import json

class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	
    @commands.command()
      async def memberCount(self, ctx):
        members=ctx.guild.member_count
        embed1=discord.Embed(title=f"members in {ctx.guild.name}",description=f"This server has {members} members",color=(0xffff00))
        await ctx.send(embed=embed1)
	
# Toni_BossOfficial added these

    @commands.command()
      async def meme(self, ctx):
	
	def get_meme():
  	    url = "https://meme-api.herokuapp.com/gimme"
  	    response = json.loads(requests.request("GET", url).text)
  	    meme_large = response["preview"][-2]
  	    subreddit = response["subreddit"]
  	    return meme_large, subreddit

	meme_pic, subreddit = get_meme()
	
	embed1=discord.Embed(title=A random meme generator:, url=meme_pic, description=subreddit, color=0x2eafff)
	embed1.add_field(name=, value=, inline=False)
	embed1.set_footer(text=Developed by Toni_BossOfficial)
	await ctx.send(embed=embed1)
	
# Toni_BossOfficial touch stopped here :)


async def setup(client):
	await client.add_cog(Fun(client))
