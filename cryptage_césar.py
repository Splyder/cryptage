'''
Fait par Splyder, le 18/09/2021
'''
alphabet=[]
# Ouvrir le fichier en lecture seule
file = open("alphabet.txt", "r")
for line in file:
    #remplit la liste nommé alphabet des lettres de chaque lignes du fichier alphabet.txt
    #.rstrip() permet de supprimer les retours à la ligne
    alphabet.append(line.rstrip())
#on referme le fichier
file.close()


def césar(clef, message):

    #vérifie si la clef rentrée est un nombre entier positif
    while str(clef).isdigit()==False:
        #si la clef n'est pas un entier positif, le script demande une nouvelle clef
        clef=input("Clef invalide. Entrez un nombre entier")
    clef=int(clef)

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
