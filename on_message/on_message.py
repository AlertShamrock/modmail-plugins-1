import discord, random
from discord.ext import commands


class OnMessage(commands.Cog):
    """ Custom """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        if (message.content.lower().startswith("first")):
            await message.channel.send('Second!')
        

def setup(bot):
    bot.add_cog(OnMessage(bot))
