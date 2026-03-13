#Etant donné un nombre n, affichez "fizz" si le nombre est divisible par 3
#affichez "buzz" si le nombre est divisible par 5
# affichez "fizzbuzz" si le nombre est divisible par 3 et par 5
#opérateur modulo si division par un nombre = 0 
#parcourez tous les nombres de 1 à 100

for n in range (1,101):
    if n % 3 == 0 and n % 5 == 0:
        print(n, "fizzbuzz")
    elif n % 3 == 0:
        print(n, "fizz")
    elif n % 5 == 0:
        print(n, "buzz")
    else :   
        print(n)
