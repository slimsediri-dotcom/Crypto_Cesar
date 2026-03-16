# Étant donné un intervalle de nombres {1-50}
# affiche tous les nombres premiers entre 1 et 50.

# NB: Un nombre premier est un entier supérieur à 1
# qui n'est divisible que par 1 et par lui-même
# (eg, 2, 3, 5, 7, 11).

# TIPS: Vous pouvez tester la divisibilité d'un nombre en regardant
# que le reste de la division euclidienne est égal à 0. Vous obtenez
# ce reste grâce à l'opérateur modulo (%).
# eg. 10 % 5 == 0

start = 1
end = 50

nombres_premiers = []
for n in range(start, end + 1):
    if n <= 1:       # négatifs, 0 et 1 ne sont pas premiers
        continue     # ignore le code en-dessous et remonte au-dessus   
    premier = True
    for i in range(2, n):   # On teste la divisibilité nbre par nbre entre 2 et n
        if n % i == 0:
            premier = False
            break           # le break arrête seulement la boucle i, on reprend ensuite à la boucle n
    if premier == True:
        nombres_premiers.append(n)
print(nombres_premiers)       
        