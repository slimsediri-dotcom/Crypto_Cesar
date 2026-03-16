# Étant donné un mot
# vérifie s’il est un palindrome (eg, radar, kayak).

# NB: Un palindrome désigne une phrase ou un mot pouvant se lire de
# gauche à droite, ou inversement, tout en gardant le même sens

# TIPS: Vous pouvez inverer l'ordre des lettres graĉe au "slicing"
# https://blog.stephane-robert.info/docs/developper/programmation/python/slicing

word = "kayak"
reversed_word = word[::-1]
if reversed_word == word:
    print(f"{word} est un palindrome")
else: print(f"{word} n'est pas un palindrome")
