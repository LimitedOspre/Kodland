meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "ROFL": "odpowiedź na żart",
            "SHEESH": "lekka dezaprobata",
            "CREEPY": "straszny, złowieszczy",
            }
word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict.keys():
    print(word, ":", meme_dict[word])
else:
    print("nie rozummiem")
