import discord
from discord import app_commands
import os
from yaml_parser import admins, mods, restricted_users
from dotenv import load_dotenv
load_dotenv()
guild_id = discord.Object(id=os.environ.get('guild-id'))
print(admins)

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        print(f'Logged on as {self.user}!')

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=guild_id)
        await self.tree.sync(guild=guild_id)

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

client.run(os.environ.get('bot-token'))