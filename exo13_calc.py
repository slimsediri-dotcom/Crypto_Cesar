# créez le script "calc.py" qui s'utilise comme suit :

#calc.py + 1 5
#calc.py + 7 5 6 12
#calc.py - 4 2 1
#calc.py * 7 5
#il doit prendre en premier paramètre '+', '-' ou '*' et prendre au minimum 2 arguments supplémentaires
#il doit ensuite afficher le résultat de l'opération
# par exempl - 12 4 1 doit afficher "7" 

import sys

sys.argv.pop(0) # enlever le nom du script

#Vérification de la validité des entrées
if len(sys.argv) < 3: # vérifier qu'il y a au moins 3 arguments (opérateur et 2nombres)
    print("Il faut entrer un opérateur et au moins deux nombres")
    exit(1)

operation = sys.argv.pop(0)
if operation not in ["+", "-", "*"]: # vérifier qu'un opérateur valide est introduit
    print("Il faut un opérateur (+, - ou *)")
    exit(1)

nombres = []
for arg in sys.argv:
    if not arg.isdigit():
        print("Vous devez introduire uniquement des nombres")
        exit(1)
        
    nombres.append(float(arg))

# calcul et affichage resultat
resultat = nombres[0]

if operation == "+":
    for n in nombres[1:]:
        resultat = resultat + n

elif operation == "-":
    for n in nombres[1:]:
        resultat = resultat - n

elif operation == "*":
    for n in nombres[1:]:
        resultat = resultat * n

print(resultat)