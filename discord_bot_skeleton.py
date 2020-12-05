import discord
import time
import asyncio
from discord.ext import commands
bot = commands.Bot(command_prefix = '.')
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot is online')


@bot.command()
async def ping(ctx, *, _=None):
    await ctx.send(f'Pong! The client latency is at {round(bot.latency * 1000)}ms')
