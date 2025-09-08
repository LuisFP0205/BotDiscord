
import discord
from discord.ext import commands
import random
import asyncio

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='time')
    async def sortear(self, ctx, num_times: int):
        """Sorteia os participantes da call em n times e cria canais de voz para cada time.

        Args:
            ctx (commands.Context): O contexto do comando.
            num_times (int): O número de times a serem formados.
        """
        if not ctx.author.voice:
            await ctx.send("Você precisa estar em uma call para eu pegar os participantes.")
            return

        if num_times < 2:
            await ctx.send("O número mínimo de times é 2.")
            return

        canal = ctx.author.voice.channel
        membros = [m for m in canal.members if not m.bot]  # ignora bots
        if len(membros) < num_times:
            await ctx.send("Não há pessoas suficientes para formar esse número de times.")
            return

        # Embaralha
        random.shuffle(membros)

        # Divide em times
        times = [[] for _ in range(num_times)]
        for i, membro in enumerate(membros):
            times[i % num_times].append(membro)

        guild = ctx.guild

        # Garante que existam canais de voz para os times
        for i in range(1, num_times + 1):
            nome_canal = f"Time {i}"
            canal_time = discord.utils.get(guild.voice_channels, name=nome_canal)
            if not canal_time:
                canal_time = await guild.create_voice_channel(nome_canal, category=canal.category if canal.category else None)

            # Move os membros para o canal
            for m in times[i - 1]:
                await m.move_to(canal_time)

        # Feedback no chat
        resposta = "✅ Times sorteados!\n"
        for i, time in enumerate(times, 1):
            nomes = ", ".join([m.display_name for m in time]) if time else "Vazio"
            resposta += f"\n**Time {i}:** {nomes}"

        await ctx.send(resposta)

    @commands.command(name='reunir')
    async def reunir(self, ctx):
        """Reúne todos os participantes da call em que você está.

        Args:
            ctx (commands.Context): O contexto do comando.
        """
        if not ctx.author.voice:
            await ctx.send("Você precisa estar em uma call para reunir todos.")
            return

        destino = ctx.author.voice.channel
        guild = ctx.guild

        # Pega todos os membros que estão em canais de voz
        for canal in guild.voice_channels:
            for membro in canal.members:
                if not membro.bot:
                    await membro.move_to(destino)

        await ctx.send(f"✅ Todos foram movidos para **{destino.name}**")

async def setup(bot):
    await bot.add_cog(Voice(bot))


