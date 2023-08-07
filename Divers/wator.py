import random
import os
import time
import colorama
colorama.init()

VIDE = 0
POISSON = 1
REQUIN  = 2

#🦐  🦑  🦈  🐠 🌊 🐤

class Poisson:
    value = "🐤"
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Requin:
    value = "🦐"
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.matrice = []
        for i in range (0, y):
            tmp = []
            for j in range (0, x):
                tmp.append([0])
            self.matrice.append(tmp)

def randMove(pos, len):
    newPos = pos
    if random.randint(0, 2) == 0:
        if (newPos - 1) < 0:
            newPos = len - 1
        else:
            newPos -= 1
    else:
        if (newPos + 1) >= len:
            newPos = 0
        else:
            newPos += 1
    return newPos

# Start
nbPoisson = 20
nbRequin = 5

mapX = 120
mapY = 40
map = Map(mapX, mapY)

# Creation de Fishes et attribution de leurs emplacements
fishes = []
for i in range (0, nbPoisson):
    fishes.append(Poisson(random.randint(0, mapX), random.randint(0, mapY)))
sharks = []
for i in range (0, nbRequin):
    sharks.append(Requin(random.randint(0, mapX), random.randint(0, mapY)))
    
os.system("cls")
wave = "\033[96m" #"\033[96m"
for i in range (0, len(map.matrice)):
    for j in range (0, len(map.matrice[i])):
        wave += "~"
    wave += "\n"
print (wave)
while 1:
    # Creation et affichage de la matrice
    for i in range (0, nbPoisson):
        tmpX = fishes[i].x
        tmpY = fishes[i].y
        fishes[i].x = randMove(fishes[i].x, mapX)
        fishes[i].y = randMove(fishes[i].y, mapY)
        print(f"\033[{fishes[i].y};{fishes[i].x}H{fishes[i].value}")
        print(f"\033[{tmpY};{tmpX}H~~")
    for i in range (0, nbRequin):
        tmpX = sharks[i].x
        tmpY = sharks[i].y
        sharks[i].x = randMove(sharks[i].x, mapX)
        sharks[i].y = randMove(sharks[i].y, mapY)
        print(f"\033[{sharks[i].y};{sharks[i].x}H{sharks[i].value}")
        print(f"\033[{tmpY};{tmpX}H~~")
    time.sleep(0.100)
