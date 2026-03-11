# Déclarez une liste de note, transformez les notes sur 20 en note sur 100 et affichez les sous la forme
# note sur 100 = 50
# etc.
# Voici les notes à utiliser :
# 10 14 12 8 7 20

notes = [10,14,12,8,7,20]
for note in notes:  # on parcourt toutes les notes
    note_100 = note * 5 # 1 ligne pour le caclul
    print("note sur 100" + str(note_100))  # 1 ligne pour l'affichage, plus propre de faire plusieurs opérations
    
  
