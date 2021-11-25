import discord, os , dotenv, json

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('PROTect has connected to Discord.')
    for guild in client.guilds:
        path = "servers/" + str(guild.id) + ".json"
        print(path)
        try:
            # os.mkdir(path)

            data = {
                "flags": ["flag"],
            }

            # path = path + "/settings.json"

            # os.mkdir(path)
            f = open(path, 'x')
            f = open(path, 'w')
            json.dump(data, f)
        except FileExistsError:
            path = "servers/" + str(guild.id) + "/settings.json"

client.run(TOKEN)
