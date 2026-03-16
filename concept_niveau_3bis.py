## ██████████
## LES SLICES
## ██████████

# Il est possible d'obtenir une sous-liste à partir d'une liste
# grâce aux «slices».

notes = [12, 14, 15, 16, 8, 10, 7, 14, 15]
print(notes[2:6]) # affiche les notes de 2 à 5
print(notes[:3])  # affiche les notes de 0 à 2
print(notes[3:])  # affiche les notes de 3 à la fin

## ██████████████
## LES EXCEPTIONS
## ██████████████

# Lorsqu'une situation imprévue est idéntifiée, par exemple dans une
# précondition, vous pouvez lever une exception comme cela:
number = 0

if number == 0:
    raise Exception("number cannot be 0")

# L'exception va alors interrompre le script et afficher un message
# dans la sortie d'erreur standard.

# Certaines erreur sont levée directement par python.

print(1/0) # ZeroDivisionError

notes = [10]
print(notes[5]) # IndexError

# Vous pouvez gérer le comportement de python en cas d'exception grâce
# à try..except.

notes = [10]
try:
    notes[5]
except IndexError:
    print("Vous n'avez pas 5 notes")
    exit(1)

