# Écrire un programme qui prend en paramètre une liste de nombres
# (entiers ou flottants) et qui affiche la moyenne de tous les nombres
# de cette liste
import sys

sys.argv.pop(0) # permet d'enlever le premier argument "exo12_input.py" de ma liste.

notes = [] 
for arg in sys.argv:
    if not arg.isdigit(): #condition pour dire qu'on ne peut introduire que des chiffres
        print("Vous devez passer uniquement des nombres")
        exit(1)           # on arrête le programme  

    notes.append(float(arg)) # on ajoute chaque argument dans la liste avec .append, en virgule float 

avg = sum(notes)/len(notes) # calcul de la moyenne
print(round(avg, 1))        # impression avec un arrondi, un chiffre après la virgule