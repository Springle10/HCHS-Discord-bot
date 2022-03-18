# Import libraries
import discord
import asyncio
from discord.ext import commands

# Setup settings for bot
token = '*'
client = commands.Bot(command_prefix='!')

# Setup
@client.event
async def on_ready():
    print('[Logged in as {0.user}]'.format(client))

# Bot commands
@client.command()
async def test(ctx):
    await ctx.send('uwu~')

@client.command()
async def testarg(ctx, arg1):
    await ctx.send(arg1)

@client.command()
async def respond(ctx):
    await ctx.send('Say hello!')

    def check(message):
        return ('hello' in message.content.lower())

    await client.wait_for('message', check=check)

    await client.send_message(ctx.message.channel, 'Hello.')

@client.command()
async def react(ctx):
    message = await ctx.send('Give me a thumbs up 👍')

    await message.add_reaction('👍')

    def check(reaction, user):
        return user != client.user and str(reaction.emoji) == '👍'

    try:
        await client.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('🤨')
    else:
        await ctx.send('👍')

# Initialize bot
client.run(token)
