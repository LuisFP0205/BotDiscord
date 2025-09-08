
import discord
from discord.ext import commands
import os
from config import *


intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.invites = True
intents.members = True

client = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@client.event
async def on_ready():
    print("--------------------------------------------")
    print("Bot Online")
    print(client.user.name, client.user.id)
    print("--------------------------------------------")

async def load_extensions():
    initial_extensions = [
        "cogs.moderation",
        "cogs.valorant",
        "cogs.voice",
        "cogs.info",
        "cogs.utility"
    ]
    for extension in initial_extensions:
        await client.load_extension(extension)

async def main():
    async with client:
        await load_extensions()
        await client.start(BOT_TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


