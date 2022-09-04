import discord
import os
from yaml_parser import admins, mods, restricted_users
from dotenv import load_dotenv
load_dotenv()

print(admins)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ.get('bot-token'))