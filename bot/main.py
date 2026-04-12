import discord
from discord.ext import commands
import os

from bot.config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


async def load_cogs():
    for filename in os.listdir("./bot/cogs"):
        if filename.endswith(".py") and not filename.startswith("__"):
            cog = f"bot.cogs.{filename[:-3]}"
            try:
                await bot.load_extension(cog)
                print(f"Cog cargado: {cog}")
            except Exception as e:
                print(f"Error cargando {cog}: {e}")


async def main():
    async with bot:
        await load_cogs()
        await bot.start(DISCORD_TOKEN)


import asyncio
asyncio.run(main())