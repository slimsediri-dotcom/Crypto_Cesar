# Étant donnée une liste de nombres
# crée une nouvelle liste contenant uniquement les nombres pairs.

# NB: Un nombre pair est un entier divisible par 2
# (eg, 2, 4, 6, 8).

# TIPS: Vous pouvez tester la divisibilité d'un nombre en regardant
# que le reste de la division euclidienne est égal à 0. Vous obtenez
# ce reste grâce à l'opérateur modulo (%). 
# eg. 4 % 2 == 0

numbers = [1, 2, 3, 4, 5]

even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
print(even_numbers)
