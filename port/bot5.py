import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix="!", intents=intents)

current_number = 0
last_user = None
consecutive_count = 0
reset_count = 0
counting_channel_name = "counting"  # Change this to the name of your counting channel

# Add your private channel ID here
private_channel_id = 123456789012345678  # Replace with your private channel ID

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_message(message):
    global current_number
    global last_user
    global consecutive_count
    global reset_count

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
                    reset_count += 1
                    await handle_reset(message.author)
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
                reset_count += 1
                await handle_reset(message.author)
        else:
            await message.delete()
            current_number = 0
            last_user = None
            consecutive_count = 0
            reset_count += 1
            await handle_reset(message.author)

    await bot.process_commands(message)

async def handle_reset(user):
    global reset_count
    reset_count += 1
   
    # Get the private channel
    private_channel = bot.get_channel(private_channel_id)
    if private_channel:
        await private_channel.send(f'{user} has reset the counter. It has been reset {reset_count} time(s).')

@bot.command()
async def counter(ctx):
    global reset_count
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





bot.run('MTI1ODA2Mjc2NTg2NDc3OTgyNg.GkGgF7.tfXTBuFPfe-wtH22ATJZFQ5qyWVjC8eh0wSh_Y')

#MTI1ODA2Mjc2NTg2NDc3OTgyNg.GkGgF7.tfXTBuFPfe-wtH22ATJZFQ5qyWVjC8eh0wSh_Y