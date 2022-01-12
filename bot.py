import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("asd")

client.run(os.environ["DISCORD_TOKEN"])