# Reçoit une liste de nombres séparés par des virgules en argument.
# affiche le plus grand et le plus petit nombre.

# Vérifie les préconditions suivantes :
# 1. Au moins un argument est fourni
# 2. chaque élément est un nombre
# 3. chaque nombre est supérieur ou égal à 0

# TIPS: Vous pouvez transformer une chaîne de caractères en liste
# avec str.split(separator).

import sys
arguments = sys.argv[1:]

# On transforme la chaîne "10,20,5" en liste ["10", "20", "5"]
# On prend le premier argument fourni et on le découpe à chaque virgule
list_arguments = arguments[0].split(",")
numbers = []

try:
    for item in list_arguments:
        # Chaque élément doit être un nombre 
        valeur = float(item) 
        
        # Chaque élément doit être >= 0
        if valeur < 0:
            print(f"Erreur : {valeur} est inférieur à 0.")
            sys.exit(1)
            
        numbers.append(valeur)

except ValueError:
    print("Erreur : Tous les éléments doivent être des nombres.")
    sys.exit(1)

print(sys.argv)
if numbers:
    maximum = max(numbers)
    minimum = min(numbers)
    
    print(f"Liste traitée : {numbers}")
    print(f"Le plus grand nombre est : {plus_grand}")
    print(f"Le plus petit nombre est : {plus_petit}")