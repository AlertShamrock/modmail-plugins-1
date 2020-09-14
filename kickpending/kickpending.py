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
             x.ban(reason="Enemy")
s.enter(60, 1, banpending, (s,))
s.run()
   
def setup(bot):
    bot.add_cog(KickPending(bot))
