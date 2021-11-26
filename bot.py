import discord, os , dotenv, json, urlextract

from dotenv import load_dotenv

from discord.ext import commands
from discord.utils import get
import time

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='PROT')

#for suggest and suggested
suggested_flags = []
message_url = []
help_list = []

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

# deletes messages in list "word"
# @bot.event
# async def on_message(message):
#     msg_content = message.content.lower()
#     path = "servers/" + str(message.guild.id) + ".json"
#     data = json.load(open(path, 'r'))
#     flags = data['flags']
#     if any(flag in msg_content for flag in flags):
#         await message.channel.send("You used a bad word!")

# @bot.event
# async def on_message_url(message):    
#     msg_content = message.content.lower()
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

@bot.command(name='add')
async def add_to_flags(ctx, arg):
    if ctx.message.author.guild_permissions.administrator:
        path = "servers/" + str(ctx.guild.id) + ".json"
        serverSettings = json.load(open(path, 'r'))
        currentFlags = serverSettings['flags']
        currentFlags.append(arg)
        serverSettings['flags'] = currentFlags

        os.remove(path)

        f = open(path, 'x')
        f = open(path, 'w')
        json.dump(serverSettings, f)
    else:
        await ctx.send("Only admins can add to the list of flags.")


@bot.command(name='suggest')
async def suggest(ctx, arg):
    author = ctx.message.author
    Admin = get(ctx.guild.roles, name="Admin")
    msg = ctx.message.content
    flag = arg
    text = discord.Embed(
        title=f"Should this be a flag?", description=flag, color=discord.Color((0x0000FF)))
    msg = await ctx.reply(embed=text)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")
    # await author.send(f'A new poll has been made to suggest "{flag}" as a flag.')

    path = "servers/" + str(ctx.guild.id) + ".json"
    serverSettings = json.load(open(path, 'r'))
    currentSuggestedFlags = serverSettings['suggestedFlags']
    currentSuggestedFlagURLs = serverSettings['suggestedFlagURLs']
    currentSuggestedFlags.append(arg)
    currentSuggestedFlagURLs.append(msg.jump_url)
    serverSettings['suggestedFlags'] = currentSuggestedFlags
    serverSettings['suggestedFlagURLs'] = currentSuggestedFlagURLs
    os.remove(path)
    f = open(path, 'x')
    f = open(path, 'w')
    json.dump(serverSettings, f)

    suggested_flags.append(flag)
    message_url.append(msg.jump_url)

@bot.command(name='suggested')
async def suggested(ctx):
    path = "servers/" + str(ctx.guild.id) + ".json"
    serverSettings = json.load(open(path, 'r'))
    currentSuggestedFlags = serverSettings['suggestedFlags']
    currentSuggestedFlagURLs = serverSettings['suggestedFlagURLs']

    for i in range(len(currentSuggestedFlags)):
        flag = currentSuggestedFlags[i]
        url = currentSuggestedFlagURLs[i]
        # if flag in list, dont add – omit duplication
        x = f"**Word:**\n{flag}\n**Poll:**\n{url}\n"
        help_list.append(x)
    text = discord.Embed(title='Suggested Words', description=''.join(
        help_list), color=discord.Color((0xFFFF00)))
    await ctx.reply(embed=text)

# client.run(TOKEN)
bot.run(TOKEN)
