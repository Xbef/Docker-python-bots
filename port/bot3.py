import random
import time
import discord
from discord.ext import commands



# Define the intents
intents = discord.Intents.default()
intents.message_content = True

# Define the command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

responded_message_ids = set()


# Event: When the bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    global responded_message_ids
    
    # If the message is "pong" and not from this bot
    if message.content == "pong" and message.author != bot.user:
        # Check if this "pong" message has already been responded to
        if message.id not in responded_message_ids:
            time.sleep(1.2)
            await message.channel.send("ping")
            responded_message_ids.add(message.id)  # Mark this message as responded to

    # Allow Bot 2 to process commands as well
    await bot.process_commands(message)

    
    


# Run the bot with its token
bot.run('MTI1ODAyMDE0OTkzMjQ1Nzk5NA.GCl27O.7Qx8y3VnBfp5wngV8YXzBFzgYDcE900Ki9InI8')

#MTI1ODAyMDE0OTkzMjQ1Nzk5NA.GCl27O.7Qx8y3VnBfp5wngV8YXzBFzgYDcE900Ki9InI8