'''
Programme ecrit par Gregoire Otto le 18/09/2021
Dernière modification le 19/09/2021
'''

alphabet=[]
# Ouvrir le fichier en lecture seule
file = open('données/alphabet.txt', "r")
for line in file:
    #remplit la liste nommé alphabet des lettres de chaque lignes du fichier alphabet.txt
    #.rstrip() permet de supprimer les retours à la ligne
    alphabet.append(line.rstrip())
#on referme le fichier
file.close()


def césar(clef, message):
    condition=False
    while condition==False:
        clef=str(clef)
        if clef.isdigit()==False and clef[0]!="-":
            clef = input("Clef invalide. Entrez un nombre entier")
        elif clef[1:].isdigit() == False and str(clef[0])=="-":
            clef = input("Clef invalide. Entrez un nombre entier")
        else:
            condition=True
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
