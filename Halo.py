import requests as r
from bs4 import BeautifulSoup
import asyncio
import discord
from discord import app_commands
from discord.ext import commands
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
#ONLY IMPORT JSON IF STORING TOKEN IN JSON
#import json
#IMPORT TOKEN FROM ENV VAR
import os
intents = discord.Intents.all()
client =commands.Bot(command_prefix= '!',intents=intents)


@client.event
async def on_ready():
    print('Bot is ready!')
    
@client.event
async def on_member_join(member):
    print(f'{member} has joined server.')
@client.event
async def on_member_remove(member):
    print(f'{member} has left server.')

@client.command()
async def botping(ctx):
    await ctx.reply(f'Ping! {round(client.latency *1000)}ms')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)
    


@client.hybrid_command()
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason=reason)
    await ctx.reply(f'Kicked {member.mention}')


@client.hybrid_command()
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason=reason)
    await ctx.reply(f'Banned {member.mention}')


@client.hybrid_command()
async def stop(ctx):
    await ctx.reply("I'm out of here! You can check your stats later¯\_(ツ)_/¯")
    await client.close()




@client.command(name="halo")
async def test(ctx, user_name):
    
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

            #THIS ALLOWS FOR A RETRY OF THE URL 3 TIMES SINCE I WAS GETTING A CONNECTION ERROR
            session = r.Session()
            retry = Retry(connect=3, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            
            page = session.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            rankHalo = soup.find_all('div', attrs={"class","rating-entry__rank-info"})
            for j in range(len(rankHalo)):
                rank.append(rankHalo[j].text)
            return (user_name+ "'s all time PEAK ranked play info is: "+rank[0])
    
        
    await ctx.reply(extract(user_name))

# INSERT TOKEN 
#MAKE SURE TOKEN IS IN A SEPERATE FILE AND IMPORT FILENAME ABOVE (FILENAME.TOKEN_VARIABLE_NAME)
"""""
#USE BLOCK OF CODE IF LOADING TOKEN FROM JSON FILE
f = open('config.json')
data = json.load(f)
token = data["token"]

client.run(token)
"""

client.run(os.getenv("TOKEN"))
               
     




