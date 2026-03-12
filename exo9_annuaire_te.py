# Déclarez une fonction, qui prend un contact en paramètre et retourne le numéro
# de téléphone.

# un contact possède :
# - un prénom
# - un nom
# - un numéro de téléphone

# Définir le contact
contact = {
    "prenom": "julien",
    "nom": "oppliger",
    "tel": "0032 2 452 487 45"
}

# Retourner le numéro tél.
def obtenir_num_tel(contact: dict) -> str:
    return contact["tel"]

print(obtenir_num_tel(contact))