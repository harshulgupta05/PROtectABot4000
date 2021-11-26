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

@bot.command(name='add')
async def add_to_flags(ctx, arg):
    if ctx.message.author.guild_permissions.administrator:
        path = "servers/" + str(ctx.guild.id) + ".json"
        serverSettings = json.load(open(path, 'r'))
        currentFlags = serverSettings['flags']
        currentFlags.append(str(arg))
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
