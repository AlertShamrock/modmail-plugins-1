import datetime

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class Appeal(commands.Cog): 
    """Appeal system"""
    
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.command(aliases=["achannel"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def reportchannel(self, ctx, channel: discord.TextChannel):
        """Set the Appeal Channel"""
        await self.db.find_one_and_update(
                {"_id": "config"}, {"$set": {"appeal_channel": channel.id}}, upsert=True
            )
        embed = discord.Embed(
                color=discord.Color.blue())
        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(
            name="Set Channel", value=f"Successfully Set the Appeal Channel to {channel.mention}",inline=False
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["amention"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def appealmention(self, ctx, *, mention: str):
        """Sets the Appeal Mention"""
        await self.db.find_one_and_update(
                {"_id": "config"}, {"$set": {"appeal_mention": mention}}, upsert=True
            )
        embed = discord.Embed(
                color=discord.Color.blue())
        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(
            name="Changed Mention", value=f"Successfully Changed the appeal mention to {mention}",inline=False
        )
        await ctx.send(embed=embed)
        


    @commands.command()
    async def appeal(self, ctx, user: discord.Member, *, reason):
        """appeal blacklist"""
        config = await self.db.find_one({"_id": "config"})
        report_channel = config["appeal_channel"]
        setchannel = discord.utils.get(ctx.guild.channels, id=int(appeal_channel))
        try:
            report_mention = config["appeal_mention"]
            await setchannel.send(appeal_mention)
        except:
            pass

        embed = discord.Embed(
                    color=discord.Color.red())
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author("Appeal Blacklist system")
        embed.add_field(
                name="Reported By:", value=f"{ctx.author.mention} | ID: {ctx.author.id}",inline=False)
        embed.add_field(
                name="Reason", value=reason,inline=False)

        await setchannel.send(embed=embed)
        await ctx.send("Your appeal is now pending!")
                        
def setup(bot):
    bot.add_cog(Report(bot))
