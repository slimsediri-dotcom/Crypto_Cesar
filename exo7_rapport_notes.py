#Étant donné une liste de notes :
#14, 15, 10, 12, 8, 16, 11, 14, 19
#Affichez un rapport sous la forme suivante :

#Nombre de notes = 9
#Note 1 = 14/20 (Très bien)
#Note 2 = 15/20 (Très bien)
#Note 3 = 10/20 (Passable)
#Note 4 = 12/20 (Bien)
#Note 5 = 05/20 (Insuffisant)
#Note 6 = 16/20 (Excellent)
#Note 7 = 11/20 (Passable)
#Note 8 = 14/20 (Très bien)
#Note 9 = 19/20 (Excellent)
#Note minimale = 8
#Note maximale = 19
#Moyenne = 13.2 (Bien)
#Delta = 11

#Notes:

#Delta :
#C'est la différence entre la note minimale et maximale

#Mentions :
#16 - 20   = Excellent
#14 - 15.9 = Très bien
#12 - 13.9 = Bien
#10 - 11.9 = Passable
#00 - 9.9  = Insuffisant

# consigne, utiliser des fonctions: minimale, maximale d'un tableau, mention d'une note...

# def somme(a: int, b: int) -> int:   "Exemple de définition d'une fonction"
#    return a + b 

# def somme(notes: list) -> int:
#        somme = 0
#        for note in notes:
#            somme = somme + note
#        return somme
# print(somme([5, 10])
# 


def nombre(liste_notes: list):
    nombre = 0
    for note in liste_notes:
        nombre = nombre + 1
    return nombre

def calcul_max(liste_notes: list):
    for note in liste_notes:
        calcul_max = note
        if note + 1 > calcul_max:
            calcul_max = note + 1
        return calcul_min

def calcul_min(liste_notes: list):
    for note in liste_notes:
        calcul_min = note
        if note + 1 < calcul_min:
            calcul_min = note + 1
        return calcul_min

def mention(note: int):
        if note < 10:
            mention = ("(Insuffisant)")
        elif 10 <= note < 12:
            mention = ("(Passable)")
        elif 12 <= note < 14:
            mention = ("(Bien)")
        elif 14 <= note < 16:
            mention = ("(Très bien)")
        else:
            mention = ("(Excellent)")
        return mention

def delta(liste_notes):  #différence entre le max et le min de liste_notes
    delta = calcul_max - calcul_min  
    return delta

def moyenne(liste_notes):
    moyenne = sum(liste_notes)/nombre
    return moyenne

notes = [14,15,10,12,8,16,11,14,19]

print("Nombre de notes =", nombre)
for note in notes:
    print("Note =", note, mention[notes]) 
print("Note minimale =", calcul_min[notes]) 
print("Note maximale =", calcul_max[notes])
print("Moyenne =", moyenne[notes])
print("Delta =", delta)
