import discord
from discord.ext import commands
import json
import logging
import WTCSdatabase

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode='w')

with open("credentials.json") as jsonData:
    creds = json.load(jsonData)
    jsonData.close()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = '/', description="WTCS Bot BETA", intents=intents)

@bot.event
async def on_ready():
    assert bot is not None
    print(f"Logged in as {bot.user}")
    print(WTCSdatabase.getRaceByContext(1, 1, "Q"))

@bot.command("Get your driver statistics!")
async def whatsMyStats(context: commands.Context, user: discord.User | None):

    if user is None:
        user = context.me
    driverStats = WTCSdatabase.getDriverByID(user.id)
    # Gets a driver's racing stats
    await context.send(f"User {user.name} not found in database")

@bot.command("Get the statistics of a previous event by ID")
async def getRaceStatsByID(context, raceID: int):

    if raceID is not None:
        raceStats = WTCSdatabase.getRaceByID(raceID)
    else: await context.send(f"Race not found in database")

@bot.command("Get the statistics of a previous event by Season/round/event")
async def getRaceStatsByRound(context, season: int, round: int, session: str):
    if season is not None and round is not None and session is not None:
        WTCSdatabase.getRaceByContext(season, round, session)
    else: await context.send("Not enough context! Make sure to include the season (number), round (number) and session (string)!")

bot.run(creds["discordAuthToken"], log_handler=handler, log_level=logging.DEBUG)