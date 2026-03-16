# L'objectif est de craquer le mot de passe "target".

# Parcourez le fichier "wordlist.txt" et pour chaque mdp de la liste,
# comparez son hash avec la cible.

import hashlib

def hash_password(password: str) -> str:
    return hashlib\
        .sha256(password.encode('utf-8'))\
        .hexdigest()


target = "00dfb72e6375b0206c10c62e34e783c5c58787d982d2cd54eec4bccd033bc5b9"

#J'ouvre le fichier texte en mode lecture et je stocke le resultat dans uen variable passwordlist
with open("wordlist.txt", "r", encoding="utf-8") as f:
    passwordlist = f.readlines() 

# Pour chaque mot de ma liste, je hashe et compare à la target, j'affiche le mot de passe trouvé   
    for word in passwordlist:     
    # Dans mon fichier wordlist.txt, une ligne ressemble à : "  password123  \n"
    # Je nettoie du mdp tout ce qui dépasse (espaces, tabulations, sauts de ligne)
        clean_word = word.strip()
        if hash_password(clean_word) == target:
            print(f"Cracked: {clean_word}")
            break
