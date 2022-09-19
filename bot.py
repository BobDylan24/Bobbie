import sqlite3
import asyncio
import discord
from discord.ext import commands
import configs.secret as secret

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=secret.prefix, intents=intents, help_command=None)

@bot.event
async def on_ready():
    db = sqlite3.connect("database/db.sqlite")
    cursor = db.cursor()
    print("Connected to DB!")
    cursor.execute("CREATE TABLE IF NOT EXISTS guilds(guildname TEXT, guildid INTEGER)")
    print("Ran all DB commands.")
    await asyncio.sleep(2)
    print(f"Bot is online!\nLogged in as {bot.user.display_name}")

async def main():
    await bot.start(secret.token)

asyncio.run(main())