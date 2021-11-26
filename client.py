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
                    "FoxNews": "strong right bias",
                    "HuffPost": "strong left bias",
                    "MSNBC": "strong left bias",
                    "NationalReview": "strong right bias",
                    "NBC": "left leaning bias",
                    "Reuters": "no bias",
                    "DailyWire": "strong right bias",
                    "EpochTimes": "right leaning bias",
                    "Federalist": "strong right bias",
                    "Vox": "strong left bias"
                },
                "suggestedFlags": [],
                "suggestedFlagURLs": [],
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
    msg_content = message.content.lower()
    print(msg_content)
    path = "servers/" + str(message.guild.id) + ".json"
    data = json.load(open(path, 'r'))
    flags = data['flags']
    if any(flag in msg_content for flag in flags):
        await message.channel.send("You used a bad word!")

    bad_webs = data['urls']
    if "https://" in msg_content:
        name = msg_content.split("https://www.")[1].split(".com")[0]
        print(name)
        for website in bad_webs.keys():
            print(str(website))
            if str(website).lower() in name.lower():
                await message.reply(f'The url {message.author.name} has posted is for the site {website} which, according to AllSides.com has a bias of {bad_webs.get(website)}. View the linked media at your own discretion.')

# @client.event
# async def on_message_url(message):    
#     msg_content = message.content.lower()
#     print(msg_content + "urls")
#     path = "servers/" + str(message.guild.id) + ".json"
#     data = json.load(open(path, 'r'))
#     bad_webs = data['urls']
#     #if link, check it, reply to message
#     if "https://" in msg_content:
#         name = msg_content.split("https://www.")[1].split(".com")[0]
#         print(name)
#         for website in bad_webs.keys():
#             print(str(website))
#             if str(website).lower() in name.lower():
#                 await message.reply(f'The url {message.author.name} has posted is for the site {website} which, according to AllSides.com has a bias of {bad_webs.get(website)}. View the linked media at your own discretion.')


client.run(TOKEN)
