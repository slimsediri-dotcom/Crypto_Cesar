# déclarez une liste de notes et affichez toutes les notes de la forme
# 12, 15, 8, 13, 20, 7
# note = 12

# 1. déclarer le tableau
les_notes_de_la_classe = (12, 15, 8, 13, 20, 7) 
# 2. parcourir le tableau en affichant "12" puis "15,..."
for note in les_notes_de_la_classe:
    print (note)
#3. vous modifiez le print pour afficher "note = 12" puis "note = 15",...
    print ("note =" + str(note))
