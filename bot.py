import discord, os , dotenv, json

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

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



# client.run(TOKEN)
bot.run(TOKEN)
