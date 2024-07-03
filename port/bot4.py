import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix="!", intents=intents)

current_number = 0
last_user = None
reset_count = 0
counting_channel_name = "counting"  # Change this to the name of your counting channel

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_message(message):
    global current_number
    global last_user
    global reset_count

    if message.author == bot.user:
        return

    # Check if the message is in the counting channel
    if message.channel.name == counting_channel_name:
        if message.content.isdigit():
            number = int(message.content)

            if number == current_number + 1 and message.author != last_user:
                current_number = number
                last_user = message.author
            else:
                await message.delete()
                current_number = 0
                last_user = None
                reset_count += 1
                await message.channel.send(f'Invalid number or same user! The count is reset to 1.', delete_after=5)
        else:
            await message.delete()
            current_number = 0
            last_user = None
            reset_count += 1
            await message.channel.send(f'Invalid input! Only numbers are allowed. The count is reset to 1.', delete_after=5)

    await bot.process_commands(message)

@bot.command()
async def counter(ctx):
    global reset_count
    await ctx.send(f'The count has been reset {reset_count} times.')

bot.run('MTI1ODA1MjI2NDY4MjA2MTg4NQ.GwIoGY.mEwEvMrBAPDNeWKJHpV432_UptgXgp2bOqiP9M')



#MTI1ODA1MjI2NDY4MjA2MTg4NQ.GwIoGY.mEwEvMrBAPDNeWKJHpV432_UptgXgp2bOqiP9M