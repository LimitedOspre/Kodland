import random
import bcrypt
symbols = "+-/*!&$#?=@"
lowercase = "abcdefghijklnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

all_characters = symbols + lowercase + uppercase + numbers

lenght = int(input("podaj długość hasła: "))
haslo = [
            random.choice(symbols),
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(numbers)
]
while len(haslo) < lenght:
    next_char = random.choice(all_characters)
    if next_char in all_characters:
        haslo.append(next_char)

random.shuffle(haslo)

haslo_x = bcrypt.hashpw(''.join(haslo).encode(), bcrypt.gensalt())

print(f'Wygenerowane haslo: {haslo}')
print()
print(f'zahasowane haslo: {haslo_x}')