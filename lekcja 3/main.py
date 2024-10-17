import discord
import random

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

list = [":flag_pl:",":thumbsup:",":wave:,:thumbsdown:",":cold_face:",":face_with_symbols_over_mouth:",":laughing:",":poop:",":skull:",":feet:",":smiling_imp:",":thread:,:scooter:",":video_game:",":waning_gibbous_moon:",":mountain:",":floppy_disk:",":mobile_phone:",":hourglass:",":heart:",":clock1030:",":interrobang:",":chart_with_upwards_trend:",":dollar:",":triangular_flag_on_post:"]

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("elo"):
        await message.channel.send(":wave:")
    elif message.content.startswith('bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("__lista"):
        await message.channel.send(list)
    elif message.content.startswith("__los"):
        await message.channel.send(los(1))
    else:
        await message.channel.send(message.content)

def los(j):
    los = ""
    for i in range(j):
        los += random.choice(list)
    return los

client.run("token")