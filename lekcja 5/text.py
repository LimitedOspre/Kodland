f = open("lekcja 5/text.txt", "r", encoding = "utf-8")
text = f.read()
print(text)
f.close()

f2 = open("lekcja 5/text.txt", "w", encoding = "utf-8")
text_2 = "hello world"
f2.write(text_2)
f2.close()

import os

print(os.listdir("lekcja 5/images"))