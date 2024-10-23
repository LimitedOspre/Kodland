import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="__", intents=intents)
list = [":flag_pl:",":thumbsup:",":wave:,:thumbsdown:",":cold_face:",":face_with_symbols_over_mouth:",":laughing:",":poop:",":skull:",":feet:",":smiling_imp:",":thread:,:scooter:",":video_game:",":waning_gibbous_moon:",":mountain:",":floppy_disk:",":mobile_phone:",":hourglass:",":heart:",":clock1030:",":interrobang:",":chart_with_upwards_trend:",":dollar:",":triangular_flag_on_post:"]

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
async def kot(ctx, ilosc = 1):
    await ctx.send(":cat:" * ilosc)

@bot.command()
async def suma(ctx, a: int, b: int):
    await ctx.send(f"Suma {a} + {b} = {a+b}")

@bot.command()
async def różnica(ctx, a: int, b: int):
    await ctx.send(f"różnica {a} - {b} = {a-b}")

@bot.command()
async def iloczyn(ctx, a: int, b: int):
    await ctx.send(f"iloczyn {a} * {b} = {a*b}")

@bot.command()
async def iloraz(ctx, a: int, b: int):
    await ctx.send(f"iloraz {a} / {b} = {a/b}")

@bot.command()
async def oblicz(ctx, a: int, operacja: str, b: int):
    if operacja == "+":
        await ctx.send(f"Suma {a} + {b} = {a+b}")
    elif operacja == "-":
        await ctx.send(f"różnica {a} - {b} = {a-b}")
    elif operacja == "*":
        await ctx.send(f"iloczyn {a} * {b} = {a*b}")
    elif operacja == "/":
        await ctx.send(f"iloraz {a} / {b} = {a/b}")
        
@bot.command()
async def emotka(ctx, operacja: str, ile = 1):
    if operacja == "kot":
        await ctx.send(f":cat: * {ile}")
    elif operacja == "żaba":
        await ctx.send(f":frog: * {ile}")
    elif operacja == "długopis":
        await ctx.send(f":pen: * {ile}")
    elif operacja == "banknot":
        await ctx.send(f":dollar: * {ile}")

@bot.command()
async def los(ctx, ile = 1):
        await ctx.send(los(ile))

@bot.command()
async def lista(ctx):
        await ctx.send(list)

@bot.command()
async def helpp(ctx):
        await ctx.send("x - liczba podana przez urzytkownika\n__hello - hello!\n__żaba - :frog:\n__kot - :cat:\n__oblicz x + x - Suma\n__oblicz x - x - Różnica\n__oblicz x * x - iloczyn\n__oblicz x / x - iloraz\n__emotka kot lub żaba lub długopis lub banknot, x - :cat: x razy lub :frog: x razy lub :pen: x razy lub :dollar: x razy\n__los, x - losowa emotka x razy z listy pod __lista\n__list - lista emotek")

def los(j):
    los = ""
    for i in range(j):
        los += random.choice(list)
    return los

bot.run("token")
