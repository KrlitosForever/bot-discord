import discord
from discord.ext import commands
from bot.config import DISCORD_TOKEN, WELCOME_CHANNEL_ID

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.event
async def on_member_join(member):

    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if channel:
        await channel.send(
            f"👋 Bienvenido {member.mention} al servidor **{member.guild.name}**!"
        )


bot.run(DISCORD_TOKEN)