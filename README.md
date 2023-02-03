
DISCORD HALO STATS TRACKER 
#DESCRIPTION
A discord bot that scrapes halo stats

#DEPLOYMENT AND USING BOT
The bot is containerized so it is available to be hosted on hosting platform of your choice
EX: can be hosted using free tiers of GCP, AWS, or smaller hosting websites 
SEE LINK FOR MORE INFO ON HOSTING PLATFORMS: https://www.geeksgyaan.com/2021/12/discord-bot-hosting.html

#HOW TO OBTAIN DISCORD TOKEN
https://www.writebots.com/discord-bot-token/

#SAVE TOKEN TO ENV VARIABLE
First you need to create a docker hub and initiate repo then tag repo with image
TO SAVE discord TOKEN TO ENV VARIABLE use command docker run -e TOKEN=YOUR_TOKEN_HERE -d DockerHubUserName/RepositorName


#BOT FEATURES
main command is done by putting !halo XBOXLIVEUSERNAME in discord server bot is invited to
!clear ----> clears messages
!kick ------> kicks members
!ban ------> bans members
!botping ------>obtains ping of bot
