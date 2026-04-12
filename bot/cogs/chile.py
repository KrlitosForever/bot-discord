import discord
from discord.ext import commands, tasks
from datetime import date, datetime, time, timedelta
from bot.config import WELCOME_CHANNEL_ID # Usaremos el mismo canal de bienvenida o define uno nuevo

class Chile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.feriados_2026 = [
            {"fecha": date(2026, 5, 1), "nombre": "Día del Trabajador (Irrenunciable)"},
            {"fecha": date(2026, 5, 21), "nombre": "Día de las Glorias Navales"},
            {"fecha": date(2026, 6, 21), "nombre": "Día Nacional de los Pueblos Indígenas"},
            {"fecha": date(2026, 6, 29), "nombre": "San Pedro y San Pablo"},
            {"fecha": date(2026, 7, 16), "nombre": "Día de la Virgen del Carmen"},
            {"fecha": date(2026, 8, 15), "nombre": "Asunción de la Virgen"},
            {"fecha": date(2026, 9, 18), "nombre": "Independencia Nacional (Irrenunciable)"},
            {"fecha": date(2026, 9, 19), "nombre": "Glorias del Ejército (Irrenunciable)"},
            {"fecha": date(2026, 10, 12), "nombre": "Encuentro de Dos Mundos"},
            {"fecha": date(2026, 10, 31), "nombre": "Día de las Iglesias Evangélicas"},
            {"fecha": date(2026, 11, 1), "nombre": "Día de Todos los Santos"},
            {"fecha": date(2026, 12, 8), "nombre": "Inmaculada Concepción"},
            {"fecha": date(2026, 12, 25), "nombre": "Navidad (Irrenunciable)"}
        ]
        # Iniciar la tarea automática
        self.revisar_feriados.start()

    def cog_unload(self):
        self.revisar_feriados.cancel()

    # Se ejecuta todos los días a las 09:00 AM
    @tasks.loop(time=time(hour=9, minute=0))
    async def revisar_feriados(self):
        # Mañana será...
        manana = date.today() + timedelta(days=1)
        
        # Buscar si mañana es feriado
        feriado_manana = next((f for f in self.feriados_2026 if f["fecha"] == manana), None)

        if feriado_manana:
            canal = self.bot.get_channel(WELCOME_CHANNEL_ID)
            if canal:
                embed = discord.Embed(
                    title="📢 ¡Mañana es Feriado!",
                    description=f"Recuerden que mañana **{manana.strftime('%d/%m/%Y')}** es feriado en Chile.",
                    color=discord.Color.blue()
                )
                embed.add_field(name="Motivo", value=feriado_manana["nombre"])
                embed.set_footer(text="¡A disfrutar el descanso!")
                
                await canal.send(embed=embed)

    @commands.command(name="feriados")
    async def feriados(self, ctx):
        # ... (aquí mantienes el código del comando anterior para consulta manual)
        hoy = date.today()
        proximos = [f for f in self.feriados_2026 if f["fecha"] >= hoy][:3]
        
        embed = discord.Embed(title="🇨🇱 Próximos Feriados", color=discord.Color.red())
        for f in proximos:
            embed.add_field(name=f["nombre"], value=f["fecha"].strftime('%d/%m/%Y'), inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Chile(bot))