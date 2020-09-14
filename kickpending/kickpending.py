import datetime
import logging

logger = logging.getLogger("Modmail")

import discord
import typing
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


import sched, time
s = sched.scheduler(time.time, time.sleep)
def banpending(sc): 
        role = ctx.guild.get_role(754859445766586419)
        for x in role.members:
            await x.ban(reason="Enemy")
            await ctx.send("Kicked all members with role Pending")
        
        config = await self.db.find_one({"_id": "config"})

        if config is None:
            return await ctx.send("There's no configured log channel.")
        else:
            channel = ctx.guild.get_channel(int(config["channel"]))

        if channel is None:
            await ctx.send("There is no configured log channel.")
            return

        try:
            for member in members:
                await member.kick(reason=f"{reason if reason else None}")
                embed = discord.Embed(
                    color=discord.Color.red(),
                    title=f"{member} was kicked!",
                    timestamp=datetime.datetime.utcnow(),
                )

                embed.add_field(
                    name="Moderator", value=f"Judge Anthony", inline=False,
                )

                if reason is not None:
                    embed.add_field(name="Reason", value=reason, inline=False)

                    await ctx.send(f" {member} is now ban!")
                    await channel.send(embed=embed)
        except:
            return
s.enter(60, 1, banpending, (s,))
s.run()
   
def setup(bot):
    bot.add_cog(KickPending(bot))
