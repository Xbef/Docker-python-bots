import random
import time
import discord
from discord.ext import commands

responded_message_ids = set()

# Define the intents
intents = discord.Intents.default()
intents.message_content = True

# Define the command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: When the bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'I am {bot.user.name} (ID: {bot.user.id})')
    print('------')

# Command: Respond to !ping with pong
@bot.command()
async def hello(ctx):
    await ctx.send('hello world')
    
@bot.command()
async def Hello(ctx):
    await ctx.send('Hello World')