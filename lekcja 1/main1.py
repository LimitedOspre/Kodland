# Zaskocz swoich rówieśników!
'''import random
fakty = ["moim ulubionym daniem jest spagetti carbonara","moim ulubionym zwierzeńciem jest pies","moim ulubioną czynnością jest jazda na rowerze","jestem dummny z projektu końcowego z poprzedniego kursu"]
print(random.choice(fakty))'''
import time
import random
fakty = []
for i in range(3):
    fakt = input('dodaj informacje o sobie: ')
    fakty.append(fakt)
    print(fakty)

print('losowanie')
time.sleep(3)
print('losowy fakt to', rando.chice(fakty))
