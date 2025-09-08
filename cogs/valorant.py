
import discord
from discord.ext import commands
from config import MAPAS, AGENTS
import random

class Valorant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mapa')
    async def sortear_mapa(self, ctx):
        """Sorteia um mapa aleatório do Valorant."""
        mapa_sorteado = random.choice(MAPAS)
        await ctx.send(f"🎲 O mapa sorteado é: **{mapa_sorteado}**")

    @commands.command(name='agente')
    async def sortear_agente(self, ctx):
        """Sorteia um agente aleatório do Valorant."""
        agente_sorteado = random.choice(AGENTS)
        await ctx.send(f"👤 O agente sorteado é: **{agente_sorteado}**")

async def setup(bot):
    await bot.add_cog(Valorant(bot))


