
import discord
from discord.ext import commands, tasks
import asyncio

class ChangeStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 

    @tasks.loop(seconds=10)
        await self.bot.change_presence(activity=discord.Game(name=f"Test"))
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Game(name=f"Test"))
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Game(name=f"Test"))
        await asyncio.sleep(10)

def setup(bot):
    bot.add_cog(ChangeStatus(bot))
