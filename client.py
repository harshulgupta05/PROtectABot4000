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

@client.event
async def on_message(message):
    bad_webs = ["google", "foxnews"]
    msg_content = message.content.lower()
    #if link, check it, reply to message
    if "https://" in msg_content:
        website = urlextractor.find_urls(msg_content)[0]
        name = website.split("https://")[1].split(".com")[0]
        if name.lower() in bad_webs:
            await message.reply("BAD BOO")
            
client.run(TOKEN)
