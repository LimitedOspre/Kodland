import discord
from discord.ext import commands
from discord import app_commands
from time import time
from rembg import remove
from imageai.Detection import ObjectDetection
import requests
import os
from random import randint
import aiohttp
from bs4 import BeautifulSoup


detector = ObjectDetection() # Inicjalizacja detektora obiektów

# Ustawienia bota
intents = discord.Intents.default() # Ustawienia intencji bota
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.reactions = True
bot = commands.Bot(command_prefix="__", intents=intents) # Prefix komend bota

plik = open("token.txt") # Otwieranie pliku z tokenem
token = plik.read() # Wczytywanie tokena z pliku

weather_api_key = "ed445cb9e2fc4ce0896163833253004"
News_api_key = "012df12f9019467394e9bb136d31e14c"

# Zalogowanie na bota
@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user.name}")
    try:
        synced = await bot.tree.sync()  
        print(f"Zsynchronizowano {len(synced)} komend")
    except Exception as e:
        print(f"Błąd synchronizacji: {e}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

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
    elif operacja == "^": # Potęga
        await ctx.send(f"Potęga {a} ^ {b} = {a**b}")

@bot.command() # Komenda do obliczania pierwiastka
async def pierwiastek(ctx, a: int, b: int = 2): # Domyślnie pierwiastek kwadratowy
    if a < 0:
        await ctx.send("Nie można obliczyć pierwiastka z liczby ujemnej!")
    else:
        await ctx.send(f"Pierwiastek z {a} = {a**(1/b)}") # Obliczanie pierwiastka

@bot.command() # Komenda do obliczania średniej arytmetycznej
async def srednia(ctx, *args: int):
    if len(args) == 0:
        await ctx.send("Nie podano żadnych liczb!")
    else:
        suma = sum(args)
        srednia = suma / len(args)
        await ctx.send(f"Średnia arytmetyczna {args} = {srednia}")

# Komenda __helpp w końcu nie każdy wie co jest w bocie
@bot.command()
async def helpp(ctx):
    messages = [message async for message in ctx.channel.history(limit=1)] # Pobieranie wiadomości z kanału
    for message in messages: # Pętla do usuwania wiadomości
        await message.delete() # Usuwanie wiadomości z komendą "__helpp"
    embed = discord.Embed(
        title="Lista komend bota",
        description="```𝘅 - 𝗹𝗶𝗰𝘇𝗯𝗮 𝗽𝗼𝗱𝗮𝗻𝗮 𝗽𝗿𝘇𝗲𝘇 𝘂𝘇̇𝘆𝘁𝗸𝗼𝘄𝗻𝗶𝗸𝗮\n"
                       "__helpp - tablica komend\n"
                       "__oblicz x + x - Suma\n"
                       "__oblicz x - x - Różnica\n"
                       "__oblicz x * x - iloczyn\n"
                       "__oblicz x / x - iloraz\n"
                       "__oblicz x ^ x - potęga\n"
                       "__pierwiastek x - pierwiastek\n"
                       "__srednia [x...] - średnia arytmetyczna\n"
                       "__czas - bot wskarze ci obecny czas\n"
                       "__za x (min lub h lub dni) - bot wystartuje minutnik na daną ilość czasu\n"
                       "__usuń_tło - bot usunie tło z obrazka\n"
                       "__detekcja - bot wykryje obiekty na obrazku\n"
                       "__scrap - bot wyświetli skrypt html z danej strony\n"
                       "__dell x - usunięcie x wiadomości\n"
                       "/pogoda [Miasto] - bot wyświetli pogodę w danym mieście\n"
                       "/news [Temat] - bot wyświetli losowe newsy\n"
                       "```",
        color=0x24a2b3)
    embed.set_thumbnail(url="https://raw.githubusercontent.com/LimitedOspre/Kodland/refs/heads/main/wired-outline-1330-rest-api-hover-machine.png") # Ustawienie miniaturki
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
    if jednostka not in ["min", "h", "dni", "s"]: # Sprawdzenie czy jednostka jest poprawna
        await ctx.send("Niepoprawna jednostka! Użyj s, min, h lub dni.")
        return
    elif jednostka == "s": # Jeżeli jednostka to sekundy
        cza += liczba
    elif jednostka == "min": # Jeżeli jednostka to minuty
        cza += liczba * 60
    elif jednostka == "h": # Jeżeli jednostka to godziny
        cza += (liczba * 60) * 60
    elif jednostka == "dni": # Jeżeli jednostka to dni
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
        return
    attachment = ctx.message.attachments[0]
    if not (attachment.filename.endswith(".jpg") or attachment.filename.endswith(".png")): # Sprawdzenie czy plik jest w formacie jpg lub png
        await ctx.send("Plik musi być w formacie .jpg lub .png") # jeżeli nie to wysyłamy wiadomość
        return

    input_path = f"./temp/input.{attachment.filename.split('.')[-1]}" # Ścieżka do pliku wejściowego
    output_path = "./temp/output.png" # Ścieżka do pliku wyjściowego

    # Pobieranie pliku
    async with aiohttp.ClientSession() as session: # Użycie aiohttp do pobrania pliku
        async with session.get(attachment.url) as resp: # Pobieranie pliku
            if resp.status == 200: # Sprawdzenie czy plik został pobrany poprawnie
                with open(input_path, 'wb') as f: # Otwieranie pliku do zapisu
                    f.write(await resp.read())
                await ctx.send("Obrazek jest przetwarzny, poczekaj chwilę...") # Wysyłanie wiadomości o tym że obrazek jest przerabiany

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
        return
    attachment = ctx.message.attachments[0]
    if not (attachment.filename.endswith(".jpg") or attachment.filename.endswith(".png")): # Sprawdzenie czy plik jest w formacie jpg lub png
        await ctx.send("Plik musi być w formacie .jpg lub .png") # jeżeli nie to wysyłamy wiadomość
        return

    input_path = f"./temp/input.{attachment.filename.split('.')[-1]}" # Ścieżka do pliku wejściowego
    output_path = "./temp/output.png" # Ścieżka do pliku wyjściowego

    # Pobieranie pliku
    async with aiohttp.ClientSession() as session: # Użycie aiohttp do pobrania pliku
        async with session.get(attachment.url) as resp: # Pobieranie pliku
            if resp.status == 200: # Sprawdzenie czy plik jest dostępny
                with open(input_path, 'wb') as f: # Otwieranie pliku do zapisu
                    f.write(await resp.read())
                await ctx.send("Obrazek jest przetwarzny, poczekaj chwilę...") # Wysyłanie wiadomości o tym że obrazek jest przerabiany

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
                    await ctx.send("Wykryte obiekty:" + ", ".join(detected_items))
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

@bot.command() # Komenda do wyświetlania skrypty html
async def scrap(ctx, url: str): # Komenda do wyświetlania skryptu html
    messages = [message async for message in ctx.channel.history(limit=1)] # Pobieranie wiadomości z kanału
    for message in messages: # Pętla do usuwania wiadomości
        await message.delete() # Usuwanie wiadomości z komendą "__scrap"
    response = requests.get(url) # Pobieranie strony
    if response.status_code != 200: # Sprawdzenie czy strona została pobrana poprawnie
        await ctx.send("Nie udało się pobrać strony.")
        return
    bs = BeautifulSoup(response.text, "lxml") # Pobieranie skryptu strony
    file_path = "./temp/scraped_page.html"
    with open(file_path, "w", encoding="utf-8") as f:
            f.write(bs.prettify()) # Zapisanie skryptu html do pliku
    try:
        message = await ctx.send("Oto skrypt html:", file=discord.File(file_path)) # Wysyłanie pliku na discord
        await message.add_reaction("👍")
        await message.add_reaction("👎")
    except Exception as e:
        print(f"Błąd dodawania reakcji: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

@bot.tree.command(name="pogoda") # Komenda do wyświetlania pogody
async def pogoda(interaction: discord.Interaction, miasto: str = "Warsaw"): # Komenda do wyświetlania pogody w danym mieście
    """Pobiera pogodę z API WeatherAPI i wysyła wiadomość z danymi o pogodzie."""
    url = "http://api.weatherapi.com/v1/current.json" # Adres API do pobierania pogody
    params = {
        "key": weather_api_key,
        "q": miasto,
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()

            location = data["location"]["name"] # Nazwa miasta
            temp_c = data["current"]["temp_c"] # Temperatura w stopniach Celsjusza
            temp_f = data["current"]["temp_f"] # Temperatura w stopniach Fahrenheita
            humidity = data["current"]["humidity"] # Wilgotność
            wind_kph = data["current"]["wind_kph"] # Prędkość wiatru w km/h
            wind_mph = data["current"]["wind_mph"] # Prędkość wiatru w mph
            condition = data["current"]["condition"]["text"] # Warunki pogodowe
            image_url = "http:" + data["current"]["condition"]["icon"] # Ikona pogody

            embed = discord.Embed(title=f"Pogoda w {location}", color=discord.Color.blue())
            embed.add_field(name="Temperatura", value=f"{temp_c}℃ / {temp_f}℉")
            embed.add_field(name="Wilgotność", value=f"{humidity}%")
            embed.add_field(name="Wiatr", value=f"{wind_kph} km/h / {wind_mph} mph")
            embed.add_field(name="Warunki", value=condition)
            embed.set_thumbnail(url=image_url)
            message = await interaction.response.send_message(embed=embed, ephemeral=False)
    sent_message = await interaction.original_response()
    try:
        await sent_message.add_reaction("👍")
        await sent_message.add_reaction("👎")
    except Exception as e:
        print(f"Błąd dodawania reakcji: {e}")

@bot.tree.command(name="news") # Komenda do wyświetlania newsów
async def news(interaction: discord.Interaction, query: str ="technology"): # Komenda do wyświetlania newsów
    """Pobiera newsy z API NewsAPI i wysyła wiadomość z danymi o newsach."""
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={News_api_key}&language=pl&pageSize=5'
    response = requests.get(url)
    if response.status_code != 200:
        await interaction.response.send_message("Nie udało się pobrać żadnych newsów.", ephemeral=False)
        return
    news_data = response.json()
    articles = news_data["articles"]

    if not articles:
        await interaction.response.send_message("Nie znaleziono żadnych newsów.", ephemeral=False)
        return
    news_message = f"**Oto najnowsze newsy o {query}:**\n"
    for o, article in enumerate(articles, start=randint(1, 5)):
        embed = discord.Embed(
            title=f"news o {query}",
            description=news_message,
            url=article["url"],
            color=discord.Color.blue()
        )
        embed.add_field(name="Autor", value=article["author"])
        embed.add_field(name="Tytuł", value=article["title"])
        embed.add_field(name="Opis", value=article["description"])
        embed.add_field(name="Data publikacji", value=article["publishedAt"])
        embed.add_field(name="Źródło", value=article["source"]["name"])
        embed.add_field(name="Link do artykułu", value=article["url"])

        if article["urlToImage"]:
            embed.set_image(url=article["urlToImage"])
        message = await interaction.response.send_message(embed=embed, ephemeral=False)
        break
    sent_message = await interaction.original_response()
    try:
        await sent_message.add_reaction("👍")
        await sent_message.add_reaction("👎")
    except Exception as e:
        print(f"Błąd dodawania reakcji: {e}")

bot.run(token) # Uruchomienie bota
plik.close() # Zamknięcie pliku z tokenem