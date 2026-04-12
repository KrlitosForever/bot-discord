from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear", help="Borra una cantidad específica de mensajes.")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        """Borra mensajes del canal actual (por defecto 5)."""
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"✅ Se han eliminado {amount} mensajes.", delete_after=5)

    @commands.command(name="kick", help="Expulsa a un miembro del servidor.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Expulsa a un usuario mencionado."""
        await member.kick(reason=reason)
        await ctx.send(f"👢 {member.mention} ha sido expulsado. Razón: {reason}")

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ No tienes permiso para gestionar mensajes.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))