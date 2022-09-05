import discord
import os
from utils.yaml_parser import admins, mods, restricted_users, whitelist_domains, whitelist_languages
from utils.validate import validateUrl, validateLangs
from utils.messages import error_message
from dotenv import load_dotenv
load_dotenv()

guild_id = discord.Object(id=os.environ.get('guild-id'))

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)
        print(self)

    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=guild_id)
        await self.tree.sync(guild=guild_id)
        print(f'Logged on as {self.user}!')

    async def on_ready(self):
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Challenge Submissions"))

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

def is_staff(interaction: discord.Interaction):
    if str(interaction.user.id) in restricted_users:
        return False
    if str(interaction.user.id) in admins or str(interaction.user.id) in mods:
        return True
    for x in interaction.user.roles:
        if str(x.id) in admins or str(x.id) in mods:
            return True
    return False

@client.tree.command()
@discord.app_commands.check(is_staff)
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')
@hello.error
async def hello_error(interaction: discord.Interaction, error):
    err = error_message('You do not have permission to use this command')
    await interaction.response.send_message(embed=err)
    return

# --- SUBMIT COMMAND --- #
@client.tree.command()
@discord.app_commands.describe(
    url='The url of your GitHub repository',
    languages='The list of languages you completed in this challenge',
)
async def submit(interaction: discord.Interaction, url: str, languages: str):
    """Submit your completed challenge!"""
    langs = languages.split()
    
    if len(whitelist_domains) == 0:
        err = error_message('URLs are not set up! Please check your `config.yaml`.') 
        await interaction.response.send_message(embed=err)
        return
    if len(whitelist_languages) == 0:
        err = error_message('Languages are not set up! Please check your `config.yaml`.')
        await interaction.response.send_message(embed=err)
        return
    if not validateUrl(url):
        err = error_message('Invalid URL! Our currently supported URLs are: `' + ', '.join(whitelist_domains) + '`') 
        await interaction.response.send_message(embed=err)
        return
    if not validateLangs(langs):
        err = error_message('Invalid Language(s)! Our currently supported languages are: `' + ', '.join(whitelist_languages) + '`')
        await interaction.response.send_message(embed=err)
        return

    print('valid command')

    await interaction.response.send_message(f'{url} + {languages}')

client.run(os.environ.get('bot-token'))