# Étant donné un nombre n
# affiche sa table de multiplication de 1 à 10
# sous la forme :
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# ...
# 4 x 10 = 40

n = 7
for i in range(1,11):
    resultat = n * i
    print(f"{n} x {i} = {resultat}")
