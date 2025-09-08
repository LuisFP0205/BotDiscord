
import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='comandos')
    async def comandos(self, ctx):
        """Mostra a lista de comandos disponíveis do bot."""
        mensagem = """      
**# 🧩 Comandos BOT 🧩**
**➡️ !mapa** - Sorteia um mapa do Valorant
**➡️ !time <número de times>** - Sorteia os participantes da call em n times e cria canais de voz para cada time
**➡️ !reunir** - Reúne todos os participantes da call em que você está
**➡️ !limpar <quantidade>** - Limpa a quantidade de mensagens especificada (máx 100)
**➡️ !musica_comandos** - Mostra os comandos de música
"""
        await ctx.send(mensagem)

    @commands.command(name='musica_comandos')
    async def musica_comandos(self, ctx):
        """Mostra os comandos de música."""
        musica = """      
**# 🎶 Basic commands 🎶**
**➡️ m!play** - Play a track by link or search term
**➡️ m!skip** - Skip the current track
**➡️ m!leave** - Make the bot leave the voice channel
**➡️ m!stop** - Stop the current track
"""
        await ctx.send(musica)

async def setup(bot):
    await bot.add_cog(Info(bot))




    @commands.command(name='help')
    async def help_command(self, ctx):
        """Mostra todos os comandos disponíveis do bot."""
        help_message = """**# 📚 Ajuda do Bot 📚**\n\n"""
        for cog_name, cog in self.bot.cogs.items():
            if cog_name != "Info": # Evita listar o próprio comando help duas vezes
                help_message += f"\n**__Comandos de {cog_name}:__**\n"
                for command in cog.get_commands():
                    help_message += f"➡️ `!{command.name}` - {command.help}\n"
        await ctx.send(help_message)


