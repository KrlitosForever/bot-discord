import discord
from discord.ext import commands
import aiohttp # Para peticiones asíncronas (mejor que requests para bots)

class Economia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Cambiamos la URL a la nueva API (findic.cl)
        self.url = "https://findic.cl/api/"

    @commands.command(name="economia", help="Muestra indicadores económicos de Chile (UF, Dólar, etc.)")
    async def economia(self, ctx):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.url) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        # Extraemos la fecha desde el indicador UF para mayor seguridad
                        fecha_uf = data.get('uf', {}).get('fecha', '')
                        fecha_texto = fecha_uf[:10] if fecha_uf else "el día de hoy"
                        
                        embed = discord.Embed(
                            title="🇨🇱 Indicadores Económicos Chile",
                            description=f"Valores correspondientes al {fecha_texto}",
                            color=discord.Color.green()
                        )

                        # Extraemos los datos
                        uf = data.get('uf', {}).get('valor', 'N/A')
                        dolar = data.get('dolar', {}).get('valor', 'N/A')
                        euro = data.get('euro', {}).get('valor', 'N/A')
                        utm = data.get('utm', {}).get('valor', 'N/A')
                        ipc = data.get('ipc', {}).get('valor', 'N/A')

                        # Función auxiliar para formatear los números sin crashear si el valor es 'N/A'
                        def format_val(val):
                            return f"${val:,.2f}" if isinstance(val, (int, float)) else str(val)

                        embed.add_field(name="💵 Dólar", value=format_val(dolar), inline=True)
                        embed.add_field(name="💶 Euro", value=format_val(euro), inline=True)
                        embed.add_field(name="📈 UF", value=format_val(uf), inline=True)
                        embed.add_field(name="🏛️ UTM", value=format_val(utm), inline=True)
                        embed.add_field(name="📊 IPC", value=f"{ipc}%" if ipc != 'N/A' else 'N/A', inline=True)
                        
                        embed.set_footer(text="Fuente: findic.cl")
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send(f"❌ Error al conectar con la API de indicadores (HTTP {response.status}).")
            except Exception as e:
                print(f"Error en comando economia: {e}")
                await ctx.send("⚠️ Hubo un problema al obtener o procesar los datos.")

async def setup(bot):
    await bot.add_cog(Economia(bot))