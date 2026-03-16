## █████████████ 
## LES FONCTIONS
## █████████████ 

# -- 📕 Définition
# Une fonction :
# est un bloc de code réutilisable et paramétrable.

# Elle peut prendre des paramètres et retourner une valeur.

# Pour déclarer une fonction :
#
# def nom_de_la_fonction(nom_du_parametre: type_du_parametre) -> type_de_retour:
#     return valeur_de_retour

# eg,
def somme(notes: list) -> int:
    return 0

# Pour appeler une fonction est:
#
# nom_de_la_fonction(parametre)

total = somme([12, 14, 16])

## █████████████████ 
## LES DICTIONNAIRES
## █████████████████ 

# -- 📕 Définition
# Un dictionnaire (dict) :
# est un type qui stock un ensemble de valeur sous la forme clé -> valeur.

contact = {
    "prenom": "julien",
    "nom": "oppliger",
    "tel": "0032 2 452 487 45"
}

# Pour accéder à un élément d'un dictionnaire, on utilise la même syntaxe que
# pour une liste.

contact["prenom"]

## ████████████████ 
## CLASSES & OBJETS
## ████████████████ 

# -- 📕 Définition
# Un objet :
# Est une variable composée de propriétés (variables) et de méthodes
# (fonctions).

# -- 📕 Définition
# Une classe :
# Définit la structure d'un object

# En d'autres termes une classe définit un concept général tandis
# qu'un objet représente une instance particulière de ce concept.


# Définition d'une classe voiture
class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur

    def demarrer(self):
        print(f"La {self.marque} démarre.")

    def afficher_info(self):
        print(f"Voiture: {self.marque}, Couleur: {self.couleur}")


# Création d'objets (instances de la classe)
voiture1 = Voiture("Toyota", "rouge")
voiture2 = Voiture("BMW", "noire")

# Utilisation des objets
voiture1.afficher_info()
voiture1.demarrer()
voiture2.afficher_info()

# -- 🤔 Remarque:
# En python, tout est une classe.
# Y compris, str, list, int etc.

notes = [14, 15, 8]
notes.append(12)
notes.pop(0)

firstname = "julien"
print(firstname.upper())
