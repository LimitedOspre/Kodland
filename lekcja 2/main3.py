import random
import bcrypt
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght = int(input("podaj długość hasła: "))
hasło = ""

for i in range(lenght):
    hasło += random.choice(symbols)

hasło_x = bcrypt.hashpw(hasło.encode(), bcrypt.gensalt())

print(hasło)

print(hasło_x)