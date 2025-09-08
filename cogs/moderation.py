
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='limpar')
    @commands.has_permissions(manage_messages=True)
    async def limpar(self, ctx, quantidade: int):
        """Limpa a quantidade de mensagens especificada no canal.

        Args:
            ctx (commands.Context): O contexto do comando.
            quantidade (int): O número de mensagens a serem apagadas (máximo 100).
        """
        if quantidade > 100:
            await ctx.send("Só posso deletar até 100 mensagens de uma vez!")
            return

        try:
            deleted = await ctx.channel.purge(limit=quantidade)
            mensagem = f"✅ {len(deleted)} mensagens foram apagadas!"
            await ctx.send(mensagem, delete_after=5)
        except discord.Forbidden:
            await ctx.send("Não tenho permissão para apagar mensagens neste canal.")
        except discord.HTTPException as e:
            await ctx.send(f"Ocorreu um erro ao apagar mensagens: {e}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='limpar')
    @commands.has_permissions(manage_messages=True)
    async def limpar(self, ctx, quantidade: int):
        """Limpa a quantidade de mensagens especificada no canal.

        Args:
            ctx (commands.Context): O contexto do comando.
            quantidade (int): O número de mensagens a serem apagadas (máximo 100).
        """
        if quantidade > 100:
            await ctx.send("Só posso deletar até 100 mensagens de uma vez!")
            return

        try:
            deleted = await ctx.channel.purge(limit=quantidade)
            mensagem = f"✅ {len(deleted)} mensagens foram apagadas!"
            await ctx.send(mensagem, delete_after=5)
        except discord.Forbidden:
            await ctx.send("Não tenho permissão para apagar mensagens neste canal.")
        except discord.HTTPException as e:
            await ctx.send(f"Ocorreu um erro ao apagar mensagens: {e}")




