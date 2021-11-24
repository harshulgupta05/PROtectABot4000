import discord, os , dotenv

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='PROT')

@bot.event
async def ready():
    print(f'{bot.user.name} has connected to Discord.')

bot.run(TOKEN)