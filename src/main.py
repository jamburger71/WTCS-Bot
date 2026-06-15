import discord
from discord import app_commands
from discord.ext import commands
import json
import logging
from enums import *
import pickSession
import WTCSdatabase
import YesNoPrompt

version = "0.2 Alpha Testing"

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
    assert bot.user is not None
    channel = bot.get_channel(1514948275516608512)
    await channel.send(f"The bot is now online! version: {version}")
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="stats")
@app_commands.describe(user = "Driver")
async def getstats(interaction: discord.Interaction, user: discord.Member):

    if user is None:
        user = interaction.user
    driverStats = WTCSdatabase.getDriverByID(str(user.id))
    if driverStats is None:
        if user == interaction.user:
            view = YesNoPrompt.YesNoDialogue()
            await interaction.response.send_message(embed=discord.Embed(title='Create driver data?'), view=view)
            await view.wait()
            if view.confirmed:
                await interaction.response.send_message("Yay!")
            else:
                await interaction.response.send_message("Aw.")
        else:
            interaction.response.send_message("This driver has no stats saved.")
    else:
        await interaction.response.send_message(f"Hello, {interaction.user.name}! Here are your dumped stats! {driverStats}")

@bot.tree.command(name="eventstats")
@app_commands.describe(season = "Season", round = "Round")
async def getRaceStat(interaction: discord.Interaction, season: int, round: int):
    if not int(season):
        await interaction.response.send_message("Please make sure the season is a number!")
    elif not int(round):
        await interaction.response.send_message("Please make sure the round is a number!")
    else:
        view = pickSession.PickSessionPrompt()
        await interaction.response.send_message(embed=discord.Embed(title="Which session are you entering data for?"), view=view)
        await view.wait()
        data = WTCSdatabase.getRaceByContext(season=season, round=round, session=view.type)
        print(data)
        """if view.type == SessionType.QUALI:
            
        elif view.type == SessionType.SPRINT:
            
        elif view.type == SessionType.FEATURE:"""

@bot.tree.command(name="add-race")
@app_commands.describe(season = "Season", round = "Round")
async def addRaceStat(interaction: discord.Interaction, season: int, round: int):

    if not int(season):
        await interaction.response.send_message("Please make sure the season is a number!")
    elif not int(round):
        await interaction.response.send_message("Please make sure the round is a number!")
    else:
        view = pickSession.PickSessionPrompt()
        await interaction.response.send_message(embed=discord.Embed(title="Which session are you entering data for?"), view=view)
        await view.wait()
        """if view.type == SessionType.QUALI:
            
        elif view.type == SessionType.SPRINT:
            
        elif view.type == SessionType.FEATURE:"""


bot.run(creds["discordAuthToken"], log_handler=handler, log_level=logging.DEBUG)