import discord
from discord.ext import commands
import aiohttp # Para peticiones asíncronas (mejor que requests para bots)

class Economia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = "https://mindicador.cl/api"

    @commands.command(name="economia", help="Muestra indicadores económicos de Chile (UF, Dólar, etc.)")
    async def economia(self, ctx):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.url) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        embed = discord.Embed(
                            title="🇨🇱 Indicadores Económicos Chile",
                            description=f"Valores correspondientes al {data['fecha'][:10]}",
                            color=discord.Color.green()
                        )

                        # Extraemos los datos que pediste
                        uf = data.get('uf', {}).get('valor', 'N/A')
                        dolar = data.get('dolar', {}).get('valor', 'N/A')
                        euro = data.get('euro', {}).get('valor', 'N/A')
                        utm = data.get('utm', {}).get('valor', 'N/A')
                        ipc = data.get('ipc', {}).get('valor', 'N/A')

                        embed.add_field(name="💵 Dólar", value=f"${dolar:,.2f}", inline=True)
                        embed.add_field(name="💶 Euro", value=f"${euro:,.2f}", inline=True)
                        embed.add_field(name="📈 UF", value=f"${uf:,.2f}", inline=True)
                        embed.add_field(name="🏛️ UTM", value=f"${utm:,.2f}", inline=True)
                        embed.add_field(name="📊 IPC", value=f"{ipc}%", inline=True)
                        
                        embed.set_footer(text="Fuente: mindicador.cl")
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("❌ Error al conectar con la API de indicadores.")
            except Exception as e:
                print(f"Error en comando economia: {e}")
                await ctx.send("⚠️ Hubo un problema al obtener los datos.")

async def setup(bot):
    await bot.add_cog(Economia(bot))