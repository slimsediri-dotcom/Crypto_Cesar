
## ███████████████ 
## LES EXPRESSIONS
## ███████████████ 

# -- 📕 Définition
# Une expression :
# est une instruction atomique évaluée par l'interpréteur.

# Il en existe plusieurs types comme :

# 👉 les expressions arithmétiques
1 + 1 

# 👉 les concaténations
"julien" + "oppliger"

# 👉 les expressions logiques
18 < 30
True and True

# 👉 les appels de fonction
print("Hello world !")

# 👉 les affectations de variable
a = 10

# 👉 et plein d'autres !
#   (déclaration de variable et de fonction, condition, boucle, etc.)

# -- 🤔 Remarque:
# Les expressions sont évaluées 
# les unes après les autres du plus 
# bas au plus haut dans la hierarchie.

# eg, :
print(pow(4 ,3 + pow(3 * 2, 4)))
print(pow(4 , 3 + pow(6, 4)))
print(pow(4 , 3 + 1296))
print(pow(4 , 1299))
print(11910465487876695589717869) # ..

## █████████████
## Les variables
## █████████████

# -- 📕 Définition
# La déclaration de variable :
# indique au système que la variable existe
a = "variable déclarée"

# -- 📕 Définition
# l' affectation de variable :
# indique au système que la variable contient cette valeur
a = "variable affectée"

# -- Remarque:
# En python la déclaration d'une variable 
# se fait au moment de l'affectation.

# La variable est déclarée lorsqu'elle est affectée pour la première fois.
b = "ma valeur" 
# Elle peut être réaffectée mais pas redéclarée.
b = "une autre valeur" 

## █████████ 
## LE TYPAGE
## █████████ 

# -- 📕 Définition
# Un type :
# détermine le type de valeur qu'une variable stock stock.

# Voici les principaux types de python:

# 👉 chaîne de caractères (str)
a = "une chaîne de caractères"
a = 'une chaîne de caractères'

# 👉 nombre entier (int)
entier = 10

# 👉 nombre flottant (float)
flottant = 10.0

# 👉 booléen (bool)
booleen = True
booleen = False

# -- 🤔 Remarque:
# Python est un langage a typage dynamique fort.
# Cela signifie qu'il ne va pas réaliser de conversion de type pour vous. Si une
# fonction attend une chaîne vous devez lui passer une chaîne.

# eg,
# age stock un entier (int)
age = 20 
# une concaténation attend des chaînes (str)
print("julien" + str(age))
# str(age) permet de convertir un type int en type str.

# -- 🤔 Remarque:
# Python est un langage à typage dynamique.
# Cela signigie qu'une même variable peut recevoir différents types.

# eg,
a = 10
a = "une chaîne"

## ██████████████████████████
## Les structures de contrôle
## ██████████████████████████ 

# -- 📕 Définition
# une structure de contrôle :
# permet de modifier le flux d'exécution d'un programme.

# On y trouve notamment :

# 👉 Les conditions

if age > 18:
    print("accès autorisé")
else:
    print("accès interdit")

# 👉 Les boucles

for nombre in range(0, 10):
    print("nombre = " + str(nombre))

## ██████████████
## Les conditions
## ██████████████

# Les expressions logiques

if age > 18:  # supérieur
    pass
if age >= 18: # supérieur ou égal
    pass
if age < 18:  # inférieur
    pass
if age <= 18: # inférieur ou égal
    pass
if age == 18: # égal
    pass
if age != 18: # différent
    pass

# L'opérateur "and"

if age >= 18 and age <= 25:
    print("Appliquer le tarif jeune")

#  ┌─────┬─────┬──────┐
#  │  A  │  B  │ A∧B │
#  ├─────┼─────┼──────┤
#  │  0  │  0  │  0   │
#  │  0  │  1  │  0   │
#  │  1  │  0  │  0   │
#  │  1  │  1  │  1   │
#  └─────┴─────┴──────┘

# L'opérateur "or"

if age == 18 or age == 80:
    print("bravo")

#    ┌─────┬─────┬─────┐
#    │  A  │  B  │ A∨B │
#    ├─────┼─────┼─────┤
#    │  0  │  0  │  0  │
#    │  0  │  1  │  1  │
#    │  1  │  0  │  1  │
#    │  1  │  1  │  1  │
#    └─────┴─────┴─────┘

## ██████████
## Les listes
## ██████████

# -- 📕 Définition
# une liste :
# permet de stocker un ensemble ordonné de valeurs.

les_notes_de_la_classe = [12, 16, 8, 14]
# indices :               0   1   2  3

# -- 🤔 Remarque:
# On peut accéder aux éléments d'une liste grâce à leur indice.
# L'indice commence toujours à 0 et termine toujours à la taille du tableau - 1.

## ███████████
## Les boucles
## ███████████

# -- 📕 Définition
# une boucle :
# permet de répéter un bloc d'instructions

# La syntaxe est :
# for ELEMENT in LIST:
#     instructions

for note in les_notes_de_la_classe:
    print(note)

## -- 🤔 Remarque:
# Pour répéter une opération 10 fois, vous pouvez 
# générer une liste de [0 à 10] (10 exclu) 
# grâce à la fonction "range"

for index in range(0, 10):
    print("Rentrez vous ça dans la tête")
