# Étant donné une liste de notes :
# 14, 15, 10, 12, 8, 16, 11, 14, 19
# Affichez un rapport sous la forme suivante :

# Nombre de notes = 9
# Note 1 = 14/20 (Très bien)
# Note 2 = 15/20 (Très bien)
# Note 3 = 10/20 (Passable)
# Note 4 = 12/20 (Bien)
# Note 5 = 08/20 (Insuffisant)
# Note 6 = 16/20 (Excellent)
# Note 7 = 11/20 (Passable)
# Note 8 = 14/20 (Très bien)
# Note 9 = 19/20 (Excellent)
# Note minimale = 8
# Note maximale = 19
# Moyenne = 13.2 (Bien)
# Delta = 11

# Notes:

# Delta :
# C'est la différence entre la note minimale et maximale

# Mentions :
# 16 - 20   = Excellent
# 14 - 15.9 = Très bien
# 12 - 13.9 = Bien
# 10 - 11.9 = Passable
# 00 - 9.9  = Insuffisant

def compter_notes(notes: list) -> int:
    compteur = 0
    for note in notes:
        compteur = compteur + 1

    return compteur


def obtenir_mention(note: int | float) -> str:
    # préconditions
    if note < 0:
        raise Exception("La note ne peut pas être inféireur à 0")
    if note > 20:
        raise Exception("La note ne peut pas être supérieur à 20")

    # logique
    if note < 10:
        return "Insuffisant"
    elif note < 12:
        return "Passable"
    elif note < 14:
        return "Bien"
    elif note < 16:
        return "Très Bien"
    else:
        return "Excellent"
    
def obtenir_note_minimale(notes: list) -> int:
    note_minimale = 20
    for note in notes:
        if note < note_minimale:
            note_minimale = note

    return note_minimale

def obtenir_note_maximale(notes: list) -> int:
    note_maximale = 0
    for note in notes:
        if note > note_maximale:
            note_maximale = note

    return note_maximale

def calculer_somme(notes: list) -> int:
    somme = 0
    for note in notes:
        somme = somme + note
    
    return somme

def calculer_moyenne(notes: list) -> float:
    return calculer_somme(notes) / compter_notes(notes)

def calculer_delta(notes: list) -> int:
    return obtenir_note_maximale(notes) - obtenir_note_minimale(notes)

def afficher_rapport(notes):
    note_minimale = obtenir_note_minimale(notes)
    note_maximale = obtenir_note_maximale(notes)
    moyenne = calculer_moyenne(notes)
    delta = calculer_delta(notes)

    print(f"Nombre de notes = {compter_notes(notes)}")

    indice = 1
    for note in notes:
        print(f"Note {indice} = {note}/20 ({obtenir_mention(note)})")
    indice = indice + 1

    print(
        f"Note minimale = {note_minimale}\n"
        f"Note maximale = {note_maximale}\n"
        f"Moyenne = {round(moyenne, 1)} ({obtenir_mention(moyenne)})\n"
        f"Delta = {delta}\n")

notes = [14, 15, 10, 12, 8, 16, 11, 14, 19]
afficher_rapport(notes)