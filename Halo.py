import requests as r
from bs4 import BeautifulSoup
import asyncio
import discord
from discord.ext import commands
import json
client =commands.Bot(command_prefix= '!')


@client.event
async def on_ready():
    print('Bot is ready!')   
@client.event
async def on_member_join(member):
    print(f'{member} has joined server.')
@client.event
async def on_member_remove(member):
    print(f'{member} has left server.')
@client.command(name='halo')
async def test(ctx, arg):
    user_name=arg
    def urlValidity(user_name):
        url = "https://halotracker.com/halo-infinite/profile/xbl/"+user_name+"/overview"
        request_response = r. head(url)
        status_code = request_response. status_code
        website_is_up = status_code == 200.
        return website_is_up
    def extract(user_name):
        if not urlValidity(user_name):
            errorMsg = "ERROR: Not A Valid Halo Username, please check you're spelling"
            return errorMsg
        else:
            rank = []
            url = "https://halotracker.com/halo-infinite/profile/xbl/"+user_name+"/overview"
            page = r.get(url,timeout=5)
            soup = BeautifulSoup(page.content, 'html.parser')
            rankHalo = soup.find_all('div', attrs={"class","rating-entry__rank-info"})
            for j in range(len(rankHalo)):
                rank.append(rankHalo[j].text)
            return (user_name+ "'s all time PEAK ranked play info is: "+rank[0])
    await ctx.send(extract(user_name))
@client.command()
async def botPing(ctx):
    await ctx.send(f'Ping! {round(client.latency *1000)}ms')
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)
@client.command()
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')
@client.command()
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
@client.command()
async def stop(ctx):
    await ctx.send("I'm out of here! You can check your stats later¯\_(ツ)_/¯")
    await client.logout()
# INSERT TOKEN 
#MAKE SURE TOKEN IS IN A SEPERATE FILE AND IMPORT FILENAME ABOVE (FILENAME.TOKEN_VARIABLE_NAME)
f = open('config.json')
data = json.load(f)
token = data["token"]

client.run(token)



               
     




