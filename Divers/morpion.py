import os
import keyboard # A installer via pip install keyboard
import time

#samia = "\033[95m]"
#mehdi = "\033[91m]"
#mat_color = "\033[0m]"

class Player:
    def __init__(self, name, pion, player):
        self.name = name
        self.pion = pion
        self.player = player
        self.score = 0

player1Name = input("Nom Joueur 1: ")
player2Name = input("Nom Joueur 2: ")
maxGame = int(input("Nombre de Parties: "))

player1 = Player(player1Name, "X", "1")
player2 = Player(player2Name, "O", "2")

pion = player1.pion
player = player1.player
back =      "         "
matrice =   f"{pion}        "
xpos =      0

nbGame = 0
end = False
while player1.score < maxGame and player2.score < maxGame:
    os.system("cls")
    print  (" --- --- --- ")
    print (f"| {matrice[0]} | {matrice[1]} | {matrice[2]} |")
    print  (" --- --- ---")
    print (f"| {matrice[3]} | {matrice[4]} | {matrice[5]} |")
    print  (" --- --- --- ")
    print (f"| {matrice[6]} | {matrice[7]} | {matrice[8]} |")
    print  (" --- --- --- ")

    print (f"\n{player1.name}: {player1.score}, {player2.name}: {player2.score}")
    if back[xpos] == " " or end == True:
        matriceList = list(matrice)
        matriceList[xpos] = " "
        matrice = ''.join(matriceList)
        end = False
    key = keyboard.read_key()
    if key == "up" and xpos > 2:
        xpos -= 3
    elif key == "down" and xpos < 6:
        xpos += 3
    elif key == "right" and xpos != 2 and xpos != 5 and xpos != 8:
        xpos += 1
    elif key == "left" and xpos != 0 and xpos != 3 and xpos != 6:
        xpos -= 1
    elif key == "space" and back[xpos] == " ":
        backList = list(back)
        backList[xpos] = player
        back = ''.join(backList)
        matriceList = list(matrice)
        matriceList[xpos] = pion
        matrice = ''.join(matriceList)
        if (matrice[0] == pion and matrice[1] == pion and matrice[2] == pion) or (matrice[3] == pion and matrice[4] == pion and matrice[5] == pion) or (matrice[6] == pion and matrice[7] == pion and matrice[8] == pion) or \
            (matrice[0] == pion and matrice[3] == pion and matrice[6] == pion) or (matrice[1] == pion and matrice[4] == pion and matrice[7] == pion) or (matrice[2] == pion and matrice[5] == pion and matrice[8] == pion) or \
                (matrice[2] == pion and matrice[4] == pion and matrice[6] == pion) or (matrice[0] == pion and matrice[4] == pion and matrice[8] == pion):
                    if pion == player1.pion:
                        player1.score += 1
                    print (f"Les [{pion}] gagnent la partie")
                    print (f"Pressez une touche pour relancer une partie...")
                    time.sleep(0.5)
                    key = keyboard.read_key()
                    back =     f"{pion}        "
                    matrice = "         "
                    nbGame += 1
                    xpos = 0
                    end = True
        if matrice.find(" ") == -1:
            print("Match NULL !!!")
            print (f"Pressez une touche pour relancer une partie...")
            back =    f"{pion}        "
            matrice = "         "
            time.sleep(0.5)
            key = keyboard.read_key()
            xpos = 0
            end = True
        if pion == player1.pion:
            pion = player2.pion
            player = player2.player
        else:
            pion = player1.pion
            player = player1.player

    # Reset de la touche entree
    key = ""
    time.sleep(0.2)
    # Deplacement de la position du pion dans la matrice
    if back[xpos] == " " or end == True:
        matriceList = list(matrice)
        matriceList[xpos] = pion
        matrice = ''.join(matriceList)
