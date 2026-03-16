# Étant donné une phrase et un caractère,
# affiche le nombre de fois que la lettre "a" apparait

# TIPS: Vous pouvez parcourir une chaîne comme un tableau

sentence = "The quick brown fox jumps over the lazy dog"
character = "o"
compteur = 0
for i in sentence:
    if i == character:
        compteur = compteur + 1
print(f"'{character}' apparait {compteur} fois.")
