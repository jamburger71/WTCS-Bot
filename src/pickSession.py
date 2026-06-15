import discord
from discord.ext import commands
from enums import *

class PickSessionPrompt(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.type = SessionType.QUALI

    @discord.ui.button(label="Qualifying", style=discord.ButtonStyle.blurple)
    async def returnQuali(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.type = SessionType.QUALI
        self.stop()
        return True
        
    @discord.ui.button(label="Sprint", style=discord.ButtonStyle.blurple)
    async def returnSprint(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.type = SessionType.SPRINT
        self.stop()
        return False
    
    @discord.ui.button(label="Feature", style=discord.ButtonStyle.blurple)
    async def returnFeature(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.type = SessionType.FEATURE
        self.stop()
        return False