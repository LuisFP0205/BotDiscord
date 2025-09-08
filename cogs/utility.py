
import discord
from discord.ext import commands
import random

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='moeda')
    async def moeda(self, ctx):
        """Joga uma moeda (cara ou coroa)."""
        resultado = random.choice(["Cara", "Coroa"])
        await ctx.send(f"🪙 O resultado é: **{resultado}**")

async def setup(bot):
    await bot.add_cog(Utility(bot))


