# 1er exercice - factorielle
# afficher la factorielle de "number"
# factorial (10) = 1*2*3*4*5*6*7*8*9*10
# préconditions:
# - number doit être supérieur à 0
# range (min, max)

number = int(input("Entrez un nombre:"))
if number < 1:
    exit
factorial = 1
for n in range(1,(number+1))  :     #boucle
    factorial = factorial * n       #accumulateur
print("Factorielle", number,"=", factorial)