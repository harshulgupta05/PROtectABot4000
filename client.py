import discord, os , dotenv, json

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('PROTect has connected to Discord.')
    # await channel.send(f'{bot.user.name} has connected to Discord')

@client.event
async def on_join():
    for guild in client.guilds:
        path = "servers/" + str(guild.id)
        try:
            os.mkdir(path)

            data = {
                "flags": ["flag"],
                "members": guild.members,
            }

            path = path + "/settings.json"

            os.mkdir(path)
        except FileExistsError:
            path = "servers/" + str(guild.id) + "/settings.json"

client.run(TOKEN)
