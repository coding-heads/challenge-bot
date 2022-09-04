import discord
from discord import app_commands
import os
import re
import tldextract
from yaml_parser import admins, mods, restricted_users
from dotenv import load_dotenv
load_dotenv()

guild_id = discord.Object(id=os.environ.get('guild-id'))

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

# https://github.com/Rapptz/discord.py/blob/master/examples/app_commands/basic.py
@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

# --- SUBMIT COMMAND --- #
@client.tree.command()
@app_commands.describe(
    url='The url of your GitHub repository',
    languages='The list of languages you completed in this challenge',
)
async def submit(interaction: discord.Interaction, url: str, languages: str):
    """Submit you completed challenge!"""
    # verify url
    if len(url.split()) > 1:
        # Error
        return
    else:
        x = re.search("^https://{1}\S*$", url)
        if x:
            ext = tldextract.extract(url)
            print(ext.domain)

    langs = languages.split()
    # verify langs
    await interaction.response.send_message(f'{url} + {languages}')

client.run(os.environ.get('bot-token'))