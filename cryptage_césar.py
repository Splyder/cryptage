'''
Fait par Splyder, le 17/09/2021
Dernière modification le 20/09/2021
'''
import os

#la liste alphabet va contenir chaque lettre de l'alphabet.
alphabet=[]
# Ouvrir le fichier en lecture seule.
file=open('alphabet.txt', "r")
for line in file:
    #remplit la liste nommé alphabet des lettres de chaque lignes du fichier alphabet.txt.
    #.rstrip() permet de supprimer les retours à la ligne \n en python.
    alphabet.append(line.rstrip())
#on referme le fichier.
file.close()

def verification_cle(cle):

    condition=False
    while condition == False:

        #convertit la cle en string pour pouvoir ensuite utiliser la fonction .isdigit().
        cle = str(cle)

        #si la cle n'est pas un entier positif ni un entier negatif.
        if cle.isdigit() == False and cle[0] != "-":
            cle = input("Cle invalide. Entrez un nombre entier")

        #si la cle commence par moins, mais n'est pas suivi d'un entier positif.
        elif cle[1:].isdigit() == False and str(cle[0]) == "-":
            cle=input("Cle invalide. Entrez un nombre entier")

        #si la cle est un entier relatif, on arrete la boucle et on renvoit la cle.
        else:
            condition=True
            clef=int(cle)
            return clef


def cryptage_cesar(cle, message):

    clef=verification_cle(cle)

    #Change une lettre par une autre selon la cle
    def chiffrage_lettre(lettre,liste,cle):
        for e in range(len(liste)):
            if lettre ==' ':
                return ' '
            elif liste[e]==lettre:
                return str(liste[e+clef])
        #pour l'instant le programme ne peut crypter que les 26 lettres de l'alphabet français.
        return '?'

    message_chiffre = str()

    #pour chaque lettre du texte a crypter, on la crypte puis on la concatene au texte crypte.
    for lettre in message:
        message_chiffre += chiffrage_lettre(lettre,alphabet,cle)

    #puis on renvoi le message crypte.
    return(message_chiffre)

def cryptage_cesar_fichier(cle,nom_fichier,nom_fichier_crypter="crypter.txt"):
    cle=verification_cle(cle)
    nom_fichier=str(nom_fichier)
    nom_fichier_crypter=str(nom_fichier_crypter)
    f=open(str(nom_fichier),"rt")
    liste=[]
    for line in f:
        liste.append(cryptage_cesar(cle,line.rstrip()))
    f.close()

    if os.path.exists(nom_fichier_crypter)!=True:
        f2 = open(nom_fichier_crypter, "xt")
        f2.close()
    f2=open(nom_fichier_crypter,"at")

    for element in liste:
        f2.write(element+"\n")
        print(element)
