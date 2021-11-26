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
                "urls": {
                    "ABC": "left leaning bias",
                    "AlterNet": "strong left bias",
                    "Associated Press": "no bias",
                    "Axios": "no bias",
                    "BBC": "no bias",
                    "Bloomberg": "left leaning bias",
                    "Breitbart": "strong right bias",
                    "Buzzfeed": "strong left bias",
                    "CBS": "left leaning bias",
                    "CNN": "strong left bias",
                    "DailyMail": "strong right bias",
                    "Forbes": "no bias",
                    "Fox": "strong right bias",
                    "HuffPost": "strong left bias",
                    "MSNBC": "strong left bias",
                    "NationalReview": "strong right bias",
                    "NBC": "left leaning bias",
                    "Reuters": "no bias",
                    "DailyWire": "strong right bias",
                    "EpochTimes": "right leaning bias",
                    "Federalist": "strong right bias",
                    "Vox": "strong left bias"
                }
            }

            # path = path + "/settings.json"

            # os.mkdir(path)
            f = open(path, 'x')
            f = open(path, 'w')
            json.dump(data, f)
        except FileExistsError:
            path = "servers/" + str(guild.id) + "/settings.json"
            
client.run(TOKEN)
