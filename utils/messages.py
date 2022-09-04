import discord

def error_message(msg):
    embd = discord.Embed(title='Command Error!', description=msg, color=0xAB0C0C)
    embd.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Achtung.svg/628px-Achtung.svg.png')
    return embd