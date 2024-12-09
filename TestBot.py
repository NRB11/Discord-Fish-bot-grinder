import psutil
import discord
import asyncio

def is_discord_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] and 'discord' in process.info['name'].lower():
            return True
    return False

TOKEN = ''
GUILD_NAME = 'AaaaAAAaaa'
CHANNEL_NAME = 'fishing'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Find the target guild (server)
    target_guild = discord.utils.find(lambda g: g.name == GUILD_NAME, client.guilds)
    if not target_guild:
        print(f'Server "{GUILD_NAME}" not found.')
        await client.close()
        return

    # Find the target channel
    target_channel = discord.utils.find(lambda c: c.name == CHANNEL_NAME, target_guild.channels)
    if not target_channel:
        print(f'Channel "{CHANNEL_NAME}" not found in server "{GUILD_NAME}".')
        await client.close()
        return

    # Send the message
    if isinstance(target_channel, discord.TextChannel):
        await target_channel.send("Hello, world!")
        print(f'Message sent to {CHANNEL_NAME} in {GUILD_NAME}.')
    else:
        print(f'Channel "{CHANNEL_NAME}" is not a text channel.')

    await client.close()

# Run the bot
if is_discord_running():
    client.run(TOKEN)
else:
    print("Discord is not running.")
