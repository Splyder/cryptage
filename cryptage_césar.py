'''
Programme ecrit par Gregoire Otto le 17/09/2021
Dernière modification le 19/09/2021
'''
import os

alphabet=[]
# Ouvrir le fichier en lecture seule
file = open('données/alphabet.txt', "r")
for line in file:
    #remplit la liste nommé alphabet des lettres de chaque lignes du fichier alphabet.txt
    #.rstrip() permet de supprimer les retours à la ligne
    alphabet.append(line.rstrip())
#on referme le fichier
file.close()

def verification_clef(clef):
    condition = False
    while condition == False:
        clef = str(clef)
        if clef.isdigit() == False and clef[0] != "-":
            clef = input("Clef invalide. Entrez un nombre entier")
        elif clef[1:].isdigit() == False and str(clef[0]) == "-":
            clef = input("Clef invalide. Entrez un nombre entier")
        else:
            condition = True
            clef = int(clef)
            return clef


def cryptage_césar(clef, message):

    clef=verification_clef(clef)

    #Change une lettre par une autre selon la clef
    def lettre_chiffré(lettre,liste,clef):
        for e in range(len(liste)):
            if lettre ==' ':
                return ' '
            elif liste[e]==lettre:
                return str(liste[e+clef])
        return '?'

    message_chiffre = str()

    for lettre in message:
        message_chiffre += lettre_chiffré(lettre,alphabet,clef)

    return(message_chiffre)

def cryptage_césar_fichier(clef,nom_fichier,nom_fichier_crypter="crypter.txt"):
    clef=verification_clef(clef)
    nom_fichier=str(nom_fichier)
    nom_fichier_crypter=str(nom_fichier_crypter)
    f=open(str(nom_fichier),"rt")
    liste=[]
    for line in f:
        liste.append(cryptage_césar(clef,line.rstrip()))
    f.close()

    if os.path.exists(nom_fichier_crypter)!=True:
        f2 = open(nom_fichier_crypter, "xt")
        f2.close()
    f2=open(nom_fichier_crypter,"at")

    for element in liste:
        f2.write(element+"\n")
        print(element)
