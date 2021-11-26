import discord, os , dotenv, json, urlextract

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

from urlextract import URLExtract
urlextractor = URLExtract()

bot = commands.Bot(command_prefix='PROT')
# client = discord.Client()
# 
# @client.event
# async def on_ready():
#     print(f'{bot.user.name} has connected to Discord.')
#     # await channel.send(f'{bot.user.name} has connected to Discord')
# 
# @client.event
# async def on_join():
#     for guild in bot.guilds:
#         path = "servers/" + str(guild.id)
#         try:
#             os.mkdir(path)
# 
#             data = {
#                 "flags": ["flag"],
#                 "members": guild.members,
#             }
# 
#             path = path + "/settings.json"
# 
#             os.mkdir(path)
#         except FileExistsError:
#             path = "servers/" + str(guild.id) + "/settings.json"
    
@bot.command(name='add')
async def add_to_flags(ctx, arg):
    if ctx.message.author.guild_permissions.administrator:
        path = "servers/" + str(ctx.guild.id) + "/settings.json"
        serverSettings = json.load(open(path, 'r'))
        serverSettings['flags'] = serverSettings['flags'].append(arg)

        os.remove(path)

        json.dump(serverSettings, open(path, 'w'))
    else:
        await ctx.send("Only admins can add to the list of flags.")


# deletes messages in list "word"
@bot.event
async def on_message(message):
    msg_content = message.content.lower()
    path = "servers/" + str(message.guild.id) + ".json"
    data = json.load(open(path, 'r'))
    flags = data['flags']
    if any(flag in msg_content for flag in flags):
        await message.channel.send("You used a bad word!")

@bot.event
async def on_message_url(message):    
    msg_content = message.content.lower()
    path = "servers/" + str(message.guild.id) + ".json"
    data = json.load(open(path, 'r'))
    bad_webs = data['urls']
    #if link, check it, reply to message
    if "https://" in msg_content:
        name = msg_content.split("https://www.")[1].split(".com")[0]
        print(name)
        for website in bad_webs.keys():
            print(str(website))
            if str(website).lower() in name.lower():
                await message.reply(f'The url {message.author.name} has posted is for the site {website} which, according to AllSides.com has a bias of {bad_webs.get(website)}. View the linked media at your own discretion.')

# client.run(TOKEN)
bot.run(TOKEN)
