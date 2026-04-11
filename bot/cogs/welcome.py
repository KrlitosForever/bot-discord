from discord.ext import commands
from bot.config import WELCOME_CHANNEL_ID


class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        channel = self.bot.get_channel(WELCOME_CHANNEL_ID)

        if channel:
            await channel.send(
                f"👋 Bienvenido {member.mention} al servidor **{member.guild.name}**!"
            )


async def setup(bot):
    await bot.add_cog(Welcome(bot))