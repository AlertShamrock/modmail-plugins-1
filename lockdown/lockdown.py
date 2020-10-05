#Importing libraries
import discord
from discord.ext import commands

class Lockdown:
    """
    Channel lockdown commands.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True, name="lockdown")
    async def lockdown(self, ctx):
       """Lock message sending in the channel. Staff only."""
       try:
          perms = ctx.channel.overwrites_for(ctx.guild.default_role)
        perms.send_messages=False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=perms)
   
def setup(bot):
    bot.add_cog(Lockdown(bot))
