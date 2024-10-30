import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

plik = open("lekcja 5/token3.txt")
token = plik.read()

bot = commands.Bot(command_prefix="__", intents=intents)

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user.name}")

@bot.command()
async def Hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def żaba(ctx, ilosc = 5):
    await ctx.send(":frog:" * ilosc)

@bot.command()
async def img(ctx):
    with open('lekcja 5/images/1.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

import random, os
@bot.command()
async def ran_img(ctx):
    img_url = random.choice(os.listdir("lekcja 5/images"))
    with open(f'lekcja 5/images/{img_url}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def ran_index(ctx, index: int):
    img_url = os.listdir("lekcja 5/images")[index]
    with open(f'lekcja 5/images/{img_url}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

import requests
def duck_image():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data["url"]

@bot.command()
async def duck(ctx):
    img_url = duck_image()
    await ctx.send(img_url)

bot.run(token)
plik.close()