import os
import sys
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command(name='reply')
async def _reply(ctx):
    await ctx.send('I am online and listening!')


@bot.command(name='join')
async def _join(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send('You are not connected to a voice channel.')
        return
    channel = ctx.author.voice.channel
    vc = ctx.voice_client
    try:
        if vc is None:
            await channel.connect()
        else:
            await vc.move_to(channel)
        await ctx.send(f'Connected to voice channel: {channel.name}')
    except Exception as e:
        await ctx.send(f'Failed to connect: {e}')


@bot.command(name='leave')
async def _leave(ctx):
    vc = ctx.voice_client
    if vc is None:
        await ctx.send('I am not connected to any voice channel.')
        return
    try:
        await vc.disconnect()
        await ctx.send('Disconnected from voice channel.')
    except Exception as e:
        await ctx.send(f'Failed to disconnect: {e}')


@bot.command(name='shutdown')
@commands.has_permissions(administrator=True)
async def _shutdown(ctx):
    await ctx.send('Shutting down...')
    await bot.close()


@_shutdown.error
async def _shutdown_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to run this command (Administrator required).')
    else:
        await ctx.send(f'Error: {error}')


def main():
    # Production: read token from environment variable DISCORD_TOKEN (recommended)
    token = os.environ.get('DISCORD_TOKEN')
    if token:
        bot.run(token)
        return

    # Fallback (development-only): read from local file 'token.txt' if present.
    # NOTE: Do NOT commit this file to the repository. Prefer GitHub Secrets.
    fallback_path = os.path.join(os.path.dirname(__file__), 'token.txt')
    if os.path.isfile(fallback_path):
        with open(fallback_path, 'r', encoding='utf-8') as f:
            token = f.read().strip()
        if token:
            print('Using token from token.txt (development fallback)')
            bot.run(token)
            return

    print('Error: DISCORD_TOKEN environment variable not set and no token.txt found.')
    print('Set the DISCORD_TOKEN environment variable or create token.txt locally (do not commit it).')
    sys.exit(1)


if __name__ == '__main__':
    main()
