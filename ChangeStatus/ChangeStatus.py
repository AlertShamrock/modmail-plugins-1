
import discord
from discord.ext import commands, tasks
import asyncio

class ChangeStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.first = "Test"
        self.second = "Test"
        self.third = "Test"

    @tasks.loop(seconds=10)
        await self.bot.change_presence(activity=discord.Game(name=f"{self.first}"))
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Game(name=f"{self.second}"))
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Game(name=f"{self.third}"))
        await asyncio.sleep(10)

def setup(bot):
    bot.add_cog(ChangeStatus(bot))
