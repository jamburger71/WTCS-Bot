import discord
from discord.ext import commands

class YesNoDialogue(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.confirmed: bool = None

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.blurple)
    async def returnTrue(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.confirmed = True
        self.stop()
        await interaction.response.send_message("Pretending to generate user data ;)")
        return True
        
    @discord.ui.button(label="No", style=discord.ButtonStyle.blurple)
    async def returnFalse(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.confirmed = False
        self.stop()
        await interaction.response.send_message("Ok, not generating driver data.")
        return False
    
#async def Call(interaction: discord.Interaction) -> bool:
    