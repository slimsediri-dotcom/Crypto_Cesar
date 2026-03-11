#calculer la somme d'une liste de notes

notes = [15, 16, 14, 18, 13, 20, 19]
somme = 0 
for note in notes:
    somme = somme + note #concept d'accumulateur
print(somme)
