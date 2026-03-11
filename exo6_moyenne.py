# liste de notes
# Calculez la moyenne

Notes = [4,14,10,18,13,10]
total = 0
compteur = 0
for note in Notes:
    compteur = compteur + 1
    total = total + note
moyenne = total/compteur
print(moyenne)