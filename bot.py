import discord, os , dotenv

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='PROT')

@bot.event
async def ready():
    print(f'{bot.user.name} has connected to Discord.')

# deletes messages in list "word"
@bot.event
async def on_message(message):
    msg_content = message.content.lower()
    words = ["chink"]
    if any(word in msg_content for word in words):
        await message.delete()



    
bot.run(TOKEN)
