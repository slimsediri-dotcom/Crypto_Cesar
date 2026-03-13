#Etant donné un nombre n, affichez "fizz" si le nombre est divisible par 3
#affichez "buzz" si le nombre est divisible par 5
# affichez "fizzbuzz" si le nombre est divisible par 3 et par 5
#opérateur modulo si division par un nombre = 0 
#parcourez tous les nombres de 1 à 100

for n in range (1,101):
    result = ""
    if n % 3 == 0:
        result = result + "Fizz" # "1 " + "Fizz" = "1 Fizz"
    if n % 5 == 0:
        result = result + "Buzz" # "1 Fizz" + "Buzz" = "1 FizzBuzz"
       
    print(n, result)
# c'est propre; on a séparé les étapes entre construire une chaîne de caractères, tester les conditions, imprimer./n
# L'important n'est pas d'avoir quelque chose de fonctionnel mais d'avoir quelque chose de fonctionnel ET lisible ET maintenable 