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
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

# Command: Respond to !ping with pong
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.event
async def on_message(message):
    global responded_message_ids
    
    # If the message is "pong" and not from this bot
    if message.content == "ping" and message.author != bot.user:
        # Check if this "pong" message has already been responded to
        if message.id not in responded_message_ids:
            time.sleep(1.2)
            await message.channel.send("pong")
            responded_message_ids.add(message.id)  # Mark this message as responded to

    # Allow Bot 2 to process commands as well
    await bot.process_commands(message)

    

























@bot.command()
async def joke(ctx):
    jl = ["Why don't eggs tell jokes? They'd crack each other up.", 
"Why was the math book sad? It had too many problems.", 
"What do you call fake spaghetti? An impasta.", 
"Why don't some couples go to the gym? Because some relationships don't work out.", 
"What do you call a bear with no teeth? A gummy bear.", 
"Why did the scarecrow win an award? Because he was outstanding in his field.", 
"How do you organize a space party? You planet.", 
"Why don't scientists trust atoms? Because they make up everything.", 
"What do you call a fish wearing a crown? A kingfish.", 
"Why was the broom late? It swept in."]
    
    joke1 = random.choice(jl)
    
    
    await ctx.send(joke1)




# Run the bot with its token
bot.run('MTI1Nzk4NzY0MDAyOTA4OTkwMw.Gk7Wmw.oQdSHWBxzdcMZLfzezXZ6bcmq8iMEvDzuBZqKs')



#MTI1Nzk4NzY0MDAyOTA4OTkwMw.Gk7Wmw.oQdSHWBxzdcMZLfzezXZ6bcmq8iMEvDzuBZqKs