# Déclarez une liste de note
# 4 14 10 18 13 10
# affichez 
# 4 est en dessous de la moyenne
# 15 est au dessus de la moyenne
# 10 est à la moyenne
# 18 est au dessus de la moyenne
# 13 est au dessus de la moyenne
# 10 est à la moyenne
Notes = [4,14,10,18,13,10]
for note in Notes:
    if note > 10:
        print(str (note) + " > que la moyenne")
    if note == 10:
        print(str (note) + " est à la moyenne") 
    if note < 10:
        print(str (note) + " < que la moyenne")
           