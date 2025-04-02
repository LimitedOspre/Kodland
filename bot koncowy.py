# Potrzebne import'y
import discord # Importowanie discord
from discord.ext import commands # Importowanie discord.ext.commands
from time import time # Importowanie czasu
from rembg import remove # Importowanie rembg
import os # Importowanie os
import aiohttp # Importowanie aiohttp
from imageai.Detection import ObjectDetection # Importowanie imageai

detector = ObjectDetection() # Inicjalizacja detektora obiektów

# Podstawowe ustawienia bota
intents = discord.Intents.default() # Ustawienia intencji bota
intents.message_content = True # Ustawienia intencji wiadomości
plik = open("token.txt") # Otwieranie pliku z tokenem
token = plik.read() # Wczytywanie tokena z pliku
bot = commands.Bot(command_prefix="__", intents=intents) # Prefix komend bota

# Zalogowanie na bota
@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user.name}")
    try:
        synced = await bot.tree.sync()
        print(f"Zsynchronizowano {len(synced)} komend")
    except Exception as e:
        print(f"Błąd synchronizacji: {e}")

# komendy kalkulatora
@bot.command() # Komenda do obliczania sumy
async def suma(ctx, a: int, b: int):
    await ctx.send(f"Suma {a} + {b} = {a+b}")

@bot.command() # Komenda do obliczania różnicy
async def różnica(ctx, a: int, b: int):
    await ctx.send(f"różnica {a} - {b} = {a-b}")

@bot.command() # Komenda do obliczania iloczynu
async def iloczyn(ctx, a: int, b: int):
    await ctx.send(f"iloczyn {a} * {b} = {a*b}")

@bot.command() # Komenda do obliczania ilorazu
async def iloraz(ctx, a: int, b: int):
    await ctx.send(f"iloraz {a} / {b} = {a/b}")

@bot.command() # Komenda do obliczania podstawowych działań matematycznych
async def oblicz(ctx, a: int, operacja: str, b: int):
    if operacja == "+": # Suma
        await ctx.send(f"Suma {a} + {b} = {a+b}")
    elif operacja == "-": # Różnica
        await ctx.send(f"różnica {a} - {b} = {a-b}")
    elif operacja == "*": # Iloczyn
        await ctx.send(f"iloczyn {a} * {b} = {a*b}")
    elif operacja == "/": # Iloraz
        if b == 0: # Sprawdzenie czy nie dzielimy przez 0
            await ctx.send("Nie można dzielić przez 0!")
        await ctx.send(f"iloraz {a} / {b} = {a/b}")

# Komenda __helpp w końcu nie każdy wie co jest w bocie
@bot.command()
async def helpp(ctx):
    messages = [message async for message in ctx.channel.history(limit=1)] # Pobieranie wiadomości z kanału
    for message in messages: # Pętla do usuwania wiadomości
        await message.delete() # Usuwanie wiadomości
    embed = discord.Embed(
        title="Lista komend bota",
        description="```𝘅 - 𝗹𝗶𝗰𝘇𝗯𝗮 𝗽𝗼𝗱𝗮𝗻𝗮 𝗽𝗿𝘇𝗲𝘇 𝘂𝘇̇𝘆𝘁𝗸𝗼𝘄𝗻𝗶𝗸𝗮\n"
                       "__helpp - tablica komend\n"
                       "__oblicz x + x - Suma\n"
                       "__oblicz x - x - Różnica\n"
                       "__oblicz x * x - iloczyn\n"
                       "__oblicz x / x - iloraz\n"
                       "__czas - bot wskarze ci obecny czas\n"
                       "__dell x - usunięcie x wiadomości\n"
                       "__za x (min lub h lub dni) - bot wystartuje minutnik na daną ilość czasu\n"
                       "__usuń_tło - bot usunie tło z obrazka\n"
                       "__detekcja - bot wykryje obiekty na obrazku\n"
                       "```",
        color=0x24a2b3
        )
    message = await ctx.send(embed=embed)
    try:
        await message.add_reaction("👍")
        await message.add_reaction("👎")
    except Exception as e:
        print(f"Błąd dodawania reakcji: {e}")

@bot.command()
async def czas(ctx): # Komenda do wyświetlania czasu
    message = await ctx.send(f"<t:{round(time())}:F>") # Wyświetlanie czasu w formacie pełnym
    try:
        await message.add_reaction("👍")
        await message.add_reaction("👎")
    except Exception as e:
        print(f"Błąd dodawania reakcji: {e}")

@bot.command()
async def za(ctx, liczba: int , jednostka: str = "min"): # Komenda do ustawiania minutnika
    cza = round(time()) # Pobieranie aktualnego czasu
    if jednostka not in ["min", "h", "dni"]: # Sprawdzenie czy jednostka jest poprawna
        await ctx.send("Niepoprawna jednostka! Użyj min, h lub dni.")
        return
    elif jednostka == "min":
        cza += liczba * 60
    elif jednostka == "h":
        cza += (liczba * 60) * 60
    elif jednostka == "dni":
        cza += ((liczba * 60) * 60) * 24
    message = await ctx.send(f"<t:{cza}:R>")
    try:
        await message.add_reaction("👍")
        await message.add_reaction("👎")
    except Exception as e:
        print(f"Błąd dodawania reakcji: {e}")

@bot.command() # dodałem komędę do usuwania wiadomości bo mi się nie chciało tego robić ręcznie
@commands.has_permissions(manage_messages=True) # dodanie uprawnień do usuwania wiadomości
async def dell(ctx, liczba: int = 1):
    liczba += 1
    messages = [message async for message in ctx.channel.history(limit=liczba)]

    for message in messages: # Pętla do usuwania wiadomości
        await message.delete()
    
    await ctx.send(f"Usunięto {liczba - 1} wiadomości.", delete_after=3)

@bot.command()
async def usuń_tło(ctx): # Komenda do usuwania tła z obrazka
    if not ctx.message.attachments: # Sprawdzenie czy wiadomość ma załącznik
        await ctx.send("Nie wysłałeś żadnego obrazka.") 
        return # konieczenie gdy nie ma załącznika
    attachment = ctx.message.attachments[0]
    if not (attachment.filename.endswith(".jpg") or attachment.filename.endswith(".png")): # Sprawdzenie czy plik jest w formacie jpg lub png
        await ctx.send("Plik musi być w formacie .jpg lub .png") # jeżeli nie to wysyłamy wiadomość
        return # konieczenie gdy plik nie jest w formacie jpg lub png

    input_path = f"./temp/input.{attachment.filename.split('.')[-1]}" # Ścieżka do pliku wejściowego
    output_path = "./temp/output.png" # Ścieżka do pliku wyjściowego

    # Pobieranie pliku
    async with aiohttp.ClientSession() as session: # Użycie aiohttp do pobrania pliku
        async with session.get(attachment.url) as resp: # Pobieranie pliku
            if resp.status == 200: # Sprawdzenie czy plik został pobrany poprawnie
                with open(input_path, 'wb') as f: # Otwieranie pliku do zapisu
                    f.write(await resp.read())
                await ctx.send("Obrazek jest przetwarzny, czekaj chwilę...") # Wysyłanie wiadomości o tym że obrazek jest przerabiany

    try:
        # Usunięcie tła za pomocą rembg
        with open(input_path, "rb") as i:
            with open(output_path, "wb") as o:
                input_data = i.read()
                output_data = remove(input_data)
                o.write(output_data)

        # Wysyłanie przetworzonego obrazu na Discord
        with open(output_path, "rb") as f:
            message = await ctx.send("Oto obrazek z usuniętym tłem:", file=discord.File(f, "output.png"))
            try:
                await message.add_reaction("👍")
                await message.add_reaction("👎")
            except Exception as e:
                print(f"Błąd dodawania reakcji: {e}")

    except Exception as e:
        await ctx.send(f"Wystąpił błąd podczas przetwarzania obrazu: {e}")

    finally:
        # Usuwanie plików z dysku
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)

def detect_objects(image_path: str, output_path: str):
    # Ustawienia modelu detekcji obiektów
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("./AI/yolov3.pt")
    detector.loadModel()
    
    # Detekcja obiektów
    detections = detector.detectObjectsFromImage(
        input_image=image_path,
        output_image_path=output_path,
        minimum_percentage_probability=30
    )
    
    detected_items = []
    
    for detection in detections:
        name = detection["name"]
        probability = detection["percentage_probability"]
        detected_items.append(f"{name} ({probability:.2f}%)")
    
    return detected_items

@bot.command()
async def detekcja(ctx): # Komenda do detekcji obiektów na obrazku
    if not ctx.message.attachments: # Sprawdzenie czy wiadomość ma załącznik
        await ctx.send("Nie wysłałeś żadnego obrazka.") 
        return # konieczenie gdy nie ma załącznika
    attachment = ctx.message.attachments[0]
    if not (attachment.filename.endswith(".jpg") or attachment.filename.endswith(".png")): # Sprawdzenie czy plik jest w formacie jpg lub png
        await ctx.send("Plik musi być w formacie .jpg lub .png") # jeżeli nie to wysyłamy wiadomość
        return # konieczenie gdy plik nie jest w formacie jpg lub png

    input_path = f"./temp/input.{attachment.filename.split('.')[-1]}" # Ścieżka do pliku wejściowego
    output_path = "./temp/output.png" # Ścieżka do pliku wyjściowego

    # Pobieranie pliku
    async with aiohttp.ClientSession() as session: # Użycie aiohttp do pobrania pliku
        async with session.get(attachment.url) as resp: # Pobieranie pliku
            if resp.status == 200: # Sprawdzenie czy plik został pobrany poprawnie
                with open(input_path, 'wb') as f: # Otwieranie pliku do zapisu
                    f.write(await resp.read())
                await ctx.send("Obrazek jest przetwarzny, czekaj chwilę...") # Wysyłanie wiadomości o tym że obrazek jest przerabiany

    try:
        # detekcja obiektów za pomocą imageai
        detected_items = detect_objects(input_path, output_path)
        # Wysyłanie przetworzonego obrazu na Discord
        try:
            with open(output_path, "rb") as f:
                message = await ctx.send("Oto obrazek z wskazanymi rzeczani:", file=discord.File(f, "output.png"))
                try:
                    await message.add_reaction("👍")
                    await message.add_reaction("👎")
                except Exception as e:
                    print(f"Błąd dodawania reakcji: {e}")
                if not detected_items == []:
                    await ctx.send(f"Wykryte obiekty:\n {" ,".join(detected_items)}")
                else:
                    await ctx.send("Nie wykryto żadnych obiektów.")
        except FileNotFoundError:
            await ctx.send("Nie wykryto żadnych obiektów.", file=discord.File(f, input_path))
    except Exception as e:
        await ctx.send(f"Wystąpił błąd podczas przetwarzania obrazu: {e}")

    finally:
        # Usuwanie plików z dysku
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)

bot.run(token) # Uruchomienie bota
plik.close() # Zamknięcie pliku z tokenem