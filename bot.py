import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Start by typing \'!help1\''))
    print("Bot is online")


@client.command()
@commands.has_permissions(
manage_guild = True)
async def clear(ctx, ammount=10):
    await ctx.channel.purge(limit=ammount)


@client.command()
async def help1(ctx):
    await ctx.send('<@765423108717805569> hasnt told the help cmd')

@client.command(aliases=["whois", "info"])
async def user(ctx, member : discord.Member):
    embed=discord.Embed(title = member.name , description = member.mention , color = discord.Color.blue())
    embed.add_field(name = "ID" , value = member.id , inline=True)
    embed.set_thumbnail(url = member.avatar.url)
    embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

client.run('ODg3OTE5ODAxNzQ0MzU5NDI0.YULJwQ.iLTS2E7xoH9z6MxlHoiREjsDybU')
