import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix="!", intents=intents)

current_number = 0
last_user = None
consecutive_count = 0
counting_channel_name = "counting"  # Change this to the name of your counting channel

# Add your private channel ID here
private_channel_id = 1258080887049027707  # Replace with your private channel ID

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_message(message):
    global current_number
    global last_user
    global consecutive_count

    if message.author == bot.user:
        return

    # Check if the message is in the counting channel
    if message.channel.name == counting_channel_name:
        if message.content.isdigit():
            number = int(message.content)

            if message.author == last_user:
                consecutive_count += 1
                if consecutive_count == 9:
                    await message.channel.send(f'This is your last number, {message.author.mention}!')
                elif consecutive_count > 10:
                    await message.delete()
                    current_number = 0
                    last_user = None
                    consecutive_count = 0
                    await handle_reset(message.author, message.channel)
                    return
            else:
                consecutive_count = 1

            if number == current_number + 1:
                current_number = number
                last_user = message.author
            else:
                await message.delete()
                current_number = 0
                last_user = None
                consecutive_count = 0
                await handle_reset(message.author, message.channel)
        else:
            await message.delete()
            current_number = 0
            last_user = None
            consecutive_count = 0
            await handle_reset(message.author, message.channel)

    await bot.process_commands(message)

async def handle_reset(user, channel):
    # Get the private channel
    private_channel = bot.get_channel(private_channel_id)
    if private_channel:
        # Retrieve the last message in the private channel
        last_message = await private_channel.history(limit=1).flatten()
        if last_message:
            last_message_content = last_message[0].content
            match = re.search(r'has been reset (\d+) time\(s\)', last_message_content)
            if match:
                previous_reset_count = int(match.group(1))
            else:
                previous_reset_count = 0
        else:
            previous_reset_count = 0
        
        reset_count = previous_reset_count + 1
        
        await private_channel.send(f'{user.mention} has reset the counter. It has been reset {reset_count} time(s).')
    
    # Notify the counting channel about the reset
    await channel.send('Counter has been reset, start back at 1.')

@bot.command()
async def counter(ctx):
    # Get the private channel
    private_channel = bot.get_channel(private_channel_id)
    if private_channel:
        # Retrieve the last message in the private channel
        last_message = await private_channel.history(limit=1).flatten()
        if last_message:
            last_message_content = last_message[0].content
            match = re.search(r'has been reset (\d+) time\(s\)', last_message_content)
            if match:
                reset_count = int(match.group(1))
            else:
                reset_count = 0
        else:
            reset_count = 0
        
        await ctx.send(f'The count has been reset {reset_count} times.')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, number: int):
    await ctx.channel.purge(limit=number + 1)  # +1 to include the purge command message itself
    await ctx.send(f'Deleted {number} messages.', delete_after=5)

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.", delete_after=5)
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please specify a valid number of messages to delete.", delete_after=5)

# Replace 'your_token_here' with your bot's token
bot.run('your_token_here')

