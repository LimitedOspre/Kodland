import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

plik = open("lekcja 5/token3.txt")
token = plik.read()

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
        await ctx.send(":cat:"*ile)
    elif operacja == "żaba":
        await ctx.send(":frog:"*ile)
    elif operacja == "długopis":
        await ctx.send(":pen:"*ile)
    elif operacja == "banknot":
        await ctx.send(":dollar:"*ile)

@bot.command()
async def los(ctx, ile = 1):
        await ctx.send(los(ile))

@bot.command()
async def lista(ctx):
        await ctx.send(list)

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

def dog_image():
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data["url"]

@bot.command()
async def dog(ctx):
    img_url = dog_image()
    await ctx.send(img_url)

def obraz():
    n = random.randint(0, 395)
    img = f"http://dpi659qmb6hex.cloudfront.net/{n}.jpg"
    return img


@bot.command()
async def los_obraz(ctx):
    img_url = obraz()
    await ctx.send(img_url)

@bot.command()
async def pomysł_plastyczny(ctx):
    pomysly = [
        "obrazek z złużytych nakrętek",
        "motyle z rolek toaletowych",
        "ziemia z papieru i bibuły",
        "pieczątki z plasteiny",
        "drzewo z liśćmi zrobionymi z łupiny słonecznika",
        "osłonki na doniczki z plastikowej buteli",
        "świeczka z starego słoika",
        "gniazdo bocianów z wacików i włuczki",
    ]
    await ctx.send(f"twój pomysł plastyczny to {pomysly[random.randint(0, 7)]}")

@bot.command()
async def odpad(ctx, slowo: str):
    odpady = {
        "jabłko": "bio",
        "papierek": "papier",
        "puszka": "metal i tworzywa sztuczne",
        "słoik": "szkło",
        "bateria": "elektro smieci",
        "akumulator": "elektro smieci",
        "banan": "bio",
        "reklamówka": "metal i tworzywa sztuczne",
    }
    await ctx.send(f"{slowo} wyrzuca się na {odpady[slowo]}")

@bot.command()
async def rozkład(ctx, slowo: str):
    rozkłady = {
        "jabłko": "6 miesięcy",
        "papierek": "pół roku",
        "puszka": "200 lat",
        "słoik": "4000 lat",
        "bateria": "450 lat",
        "banan": "pół roku",
        "tektura": "2 lata",
        "reklamówka": "400 lat",
    }
    await ctx.send(f"{slowo} rozkłada się nawet {rozkłady[slowo]}")



@bot.command()
async def helpp(ctx):
        await ctx.send("```𝙭 - 𝙡𝙞𝙘𝙯𝙗𝙖 𝙥𝙤𝙙𝙖𝙣𝙖 𝙥𝙧𝙯𝙚𝙯 𝙪ż𝙮𝙩𝙠𝙤𝙬𝙣𝙞𝙠𝙖\n__helpp - tablica komend\n__Hello - hello!\n__żaba - 🐸🐸🐸🐸🐸\n__kot - 🐱\n__oblicz x + x - Suma\n__oblicz x - x - Różnica\n__oblicz x * x - iloczyn\n__oblicz x / x - iloraz\n__emotka kot lub żaba lub długopis lub banknot x - 🐱 x razy lub 🐸 x razy lub 🖊️ x razy lub 💵 x razy\n__los, x - losowa emotka x razy z listy pod __lista\n__lista - lista emotek\n__duck - losowe zdięcie kaczki\n__dog - losowe zdięcie psa\n__los_obraz - losowy obraz\n__pomysł_plastyczny - losowy pomysł plastyczny\n__odpad - bot wskarze ci gdzie wyrzucić odpad\n__rozkład - czas jaki rozkłada się dana rzecz```")

def los(j):
    los = ""
    for i in range(j):
        los += random.choice(list)
    return los

bot.run(token)
plik.close()