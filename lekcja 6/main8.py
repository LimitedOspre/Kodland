import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

plik = open("lekcja 6/token4.txt")
token = plik.read()

bot = commands.Bot(command_prefix="__", intents=intents)

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user.name}")

@bot.command()
async def Hello(ctx):
    await ctx.send("Hello!")

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
        "bateria": "450",
        "banan": "pół roku",
        "tektura": "2 lata",
        "reklamówka": "400 lat",
    }
    await ctx.send(f"{slowo} rozkłada się nawet {rozkłady[slowo]}")

bot.run(token)
plik.close()