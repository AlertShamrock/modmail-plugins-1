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
        elif ('help' in message.content.lower()):
                await message.channel.send('Read <#660219603212959747> !')
        elif ('test' in message.content.lower()):
                message = await message.channel.send('Read <#660219603212959747> !') 
                await message.edit(content="newcontent") 

def setup(bot):
    bot.add_cog(OnMessage(bot))
