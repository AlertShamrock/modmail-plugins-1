import discord, random
from discord.ext import commands


class OnMessage(commands.Cog):
    """ (∩｀-´)⊃━☆ﾟ.*･｡ﾟ non-commands, bot responds to specific text in channel """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
var msg = message.content.toLowerCase()
        if message.content.startwith("first"):
        
            await message.channel.send('Second!')
            # msg.add_reaction('Shamrock')

def setup(bot):
    bot.add_cog(OnMessage(bot))
