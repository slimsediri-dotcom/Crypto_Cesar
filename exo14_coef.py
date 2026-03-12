# Implémentez un script "coef.py" qui s'utilise comme suit:
# coef.py 14:2 16:2 7:1 12:4
# Afficher la moyenne pondérée de cette liste de notes sur 20

# L'objectif est de gérer toutes les erreurs possibles.
# Soit avec des préconditions, soit avec try..except
# https://docs.python.org/3/tutorial/errors.html#handling-exceptions

# NB: utilisez str.split(separator) pour séparer la note du coef
# Utiliser un dictionnaire car c'est à cela que cela sert
# https://docs.python.org/3/library/stdtypes.html#str.split

# Implémentez un script "coef.py" qui s'utilise comme suit:
# coef.py 14:2 16:2 7:1 12:4
# Afficher la moyenne pondérée de cette liste de notes sur 20

# L'objectif est de gérer toutes les erreurs possibles.
# Soit avec des préconditions, soit avec try..except
# https://docs.python.org/3/tutorial/errors.html#handling-exceptions

# NB: utilisez str.split(separator) pour séprarer la note du coef
# https://docs.python.org/3/library/stdtypes.html#str.split

import sys

sys.argv.pop(0)             #j'enlève le nom du programme

if len(sys.argv) < 1:       # je vérifie qu'il faut au moins un argument
    print("error: not enough arguments")
    exit(1)

notes = []                  # [] crée une Liste (une suite ordonnée d'éléments).
for arg in sys.argv:
    splitted = arg.split(":") # je splitte chaque argument au niveau du "i" et met dans une variable
    
    if len(splitted) != 2:   # je m'assure que splitted est bien une chaîne de 2 caractères
        print(f"error: {arg} is note a well formatted note")
        exit(1)        

    try:                    # je convertis mes arguments splittés de strings en nombres)
                            # je les range dans un dictionnaire que j'appelle note
        note = {
            "value": float(splitted[0]),
            "coef": float(splitted[1])
        }
    except ValueError:      #Je teste et gère une exception, si mon argument n'est pas un nombre
        print(f"error: {arg} must be made of numbers")
        exit(1)

    if note["value"] < 0 or note["value"] > 20: # Je vérifie que value et coef sont acceptables
        print(f"error: note {note['value']} out of range")
        exit(1)

    if note["coef"] < 0:
        print(f"error: coef {note['coef']} out of range")
        exit(1)
        
    notes.append(note)              # j'ajoute note à ma liste notes, 
                                    #notes est une liste qui contient plusieurs petits dictionnaires        

total = {
    "value": 0,
    "coef": 0
}
for note in notes:
    total["value"] = total["value"] + note["value"] * note["coef"]
    total["coef"] = total["coef"] + note["coef"]

avg = total["value"] / total["coef"]
print(avg)