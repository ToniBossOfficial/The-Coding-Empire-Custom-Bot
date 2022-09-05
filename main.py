from discord.ext import commands
import os
import discord
from asyncio import run

intents = discord.Intents()
client = commands.Bot(command_prefix = "?", intents = intents.all())

async def main():
    for f in os.listdir("./cogs"):
        if f.endswith(".py"):
            await client.load_extension("cogs." + f[:-3])

if __name__ == "__main__":
    run(main())
    f = open("token.txt", "r")

    client.run(f.read())


