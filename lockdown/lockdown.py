#Importing libraries
import discord
from discord.ext import commands

class Lockdown(commands.Cog):
    """
    Channel lockdown commands.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @commands.command(name="lockdown")
    async def lockdown(self, ctx):
       """Lock message sending in the channel. Staff only."""
       try:
            overwrites_everyone = ctx.message.channel.overwrites_for(ctx.guild.default_role)
            if overwrites_everyone.view_channel == False:
                await self.bot.say("🔒 Channel is already locked down. Use `.unlock` to unlock.")
                return
            overwrites_everyone.view_channel = False
            await self.bot.edit_channel_permissions(ctx.message.channel, ctx.guild.default_role, overwrites_everyone)
            await self.bot.say("🔒 Channel locked down. Only staff members may speak. Do not bring the topic to other channels or risk disciplinary actions.")
            msg = "🔒 **Lockdown**: {0} by {1} | {2}#{3}".format(ctx.message.channel.mention, ctx.message.author.mention, ctx.message.author.name, ctx.message.author.discriminator)
            await self.bot.send_message(self.bot.modlogs_channel, msg)
       except discord.errors.Forbidden:
            await self.bot.say("💢 I don't have permission to do this.")


    @commands.has_permissions(manage_messages=True)
    @commands.command(name="unlock")
    async def unlock(self, ctx):
       """Unlock message sending in the channel. Staff only."""
       try:
            overwrites_everyone = ctx.message.channel.overwrites_for(self.bot.everyone_role)
            overwrites_staff = ctx.message.channel.overwrites_for(self.bot.staff_role)
            if overwrites_everyone.send_messages == None:
                await self.bot.say("🔓 Channel is already unlocked.")
                return
            overwrites_everyone.send_messages = None
            overwrites_staff.send_messages = True
            await self.bot.edit_channel_permissions(ctx.message.channel, self.bot.everyone_role, overwrites_everyone)
            await self.bot.edit_channel_permissions(ctx.message.channel, self.bot.staff_role, overwrites_staff)
            await self.bot.say("🔓 Channel unlocked.")
            msg = "🔓 **Unlock**: {0} by {1} | {2}#{3}".format(ctx.message.channel.mention, ctx.message.author.mention, ctx.message.author.name, ctx.message.author.discriminator)
            await self.bot.send_message(self.bot.modlogs_channel, msg)
       except discord.errors.Forbidden:
            await self.bot.say("💢 I don't have permission to do this.")

def setup(bot):
    bot.add_cog(Lockdown(bot))
