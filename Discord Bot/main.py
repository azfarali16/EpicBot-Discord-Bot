import discord
from apikeys import *
from epic_game_api import *
from discord.ext import (commands)
import time
import schedule
import asyncio


client = commands.Bot(command_prefix ="!" , intents= discord.Intents.all())


def onlyadmin():
    """Checks for admin privileges. If not found will raise a CheckFailure error (The code will work fine)"""
    async def predicate(ctx):
        return discord.utils.get(ctx.message.author.roles, id=ADMIN_ROLE_ID) is not None
    return commands.check(predicate)

# EVENTS ----------------------------------------------------------------------------------

@client.event
async def on_ready():
    print('Bot is now ready to use!')
    print('------------------------')
    schedule_task()
    await scheduler()
    

@client.event
async def on_member_join(member):
    channel = client.get_channel(GATEWAY_LOGS_CHANNEL_ID)
    print("member joins!")
    await channel.send(f'{member.name} has joined the server!')


@client.event
async def on_member_remove(member):
    channel = client.get_channel(GATEWAY_LOGS_CHANNEL_ID)
    print('member leaves!')
    await channel.send(f'{member.name} has left the server.')

#COMMANDS ---------------------------------------------------------------------------------

@client.command()
async def hello(ctx):
    await ctx.send(f"Hi {ctx.author.nick} How do u do?")


@client.command()
@onlyadmin()
async def freeepic(ctx):
    gamelist = fetch_free_games()
    channel = client.get_channel(BOT_CHANNEL_ID)
    for game in gamelist:
        msg = game.game_info()
        await channel.send(msg)


@client.command()
@onlyadmin()
async def epicgame(ctx):
    gamelist_embeds = fetch_games_embed()
    channel = client.get_channel(FREE_GAME_CHANNEL_ID)
    await channel.send(f'@everyone Free Game Available')
    for game_embed in gamelist_embeds:
        await channel.send(embed=game_embed)


@client.command()
@onlyadmin()
async def test(ctx):
    channel = client.get_channel(BOT_CHANNEL_ID)
    emb = discord.Embed(
    colour=discord.Color.red(),
    title = "This is a title",
    description= "Embark on an epic adventure in a vast, open world teeming with mystery and danger. As the chosen hero, it's up to you to unravel ancient secrets, battle fierce monsters, and forge alliances with powerful allies. With stunning graphics, immersive gameplay, and an unforgettable story, this is the ultimate gaming experience for fans of fantasy and adventure. Are you ready to become a legend?",
    url= 'https://www.google.com',
    )

    emb.set_thumbnail(url='https://cdn1.epicgames.com/spt-assets/bf00db0c53ad40f09bc1331b34cd58b6/atom-eve-1pwm6.jpg')
    emb.set_image(url='https://cdn1.epicgames.com/spt-assets/bf00db0c53ad40f09bc1331b34cd58b6/atom-eve-nfh8q.jpg')
    emb.set_author(name='Game Company')
    emb.set_footer(text = "Original Price = 29.99$")

    emb.add_field(name='Click below to get view the link!', value='https://www.google.com' , inline=True)
    
    await channel.send(f'{ctx.author.mention} Free Game available',embed = emb)



def schedule_task():
    print('scheduling..')
    schedule.every().friday.at('12:00').do(epicgame)
    print('scheduling complete!')

async def scheduler():
    while 1:
        schedule.run_pending()
        await asyncio.sleep(1)



client.run(BOT_TOKEN)