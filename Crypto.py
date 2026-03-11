# ord et chr permettent de transformer des chiffres en caractères et inversément, table de correspondance ASCII
# aujourd'hui, on utilise unicode, plus vaste pour tenri compte de tous les alphabets y compris des emojis.
# bonjour_l = ["b","o","n", "j","o","u","r"]
# bonjour_string = "bonjour"
#print(bonjour_s[0])
#une chaîne de caractère est égale à un tableau de caractères.
# notes :
# ord("a")
# chr("68")

#pour chaque caractère
# obtenez la valeur numérique du caractère
#incrémentez cette valeur de 3
# convertissez cett evaleur en caractère
#concatenez le caractère à la chaîne ciphertext

#cleartext = "bonjour"
#ciphertext = "?"
# le chiffre de César
# pour chaque caractère
#    obtenez la valeur numérique du caractère
#    incrémentez cette valeur de 3
#    convertissez cette valeur en caractère
#    concatenez le caractère à la chaîne ciphertext

#chiffrement Cesar
def chiffrer_Cesar(cleartext: str) -> str:
    cyphertext =""
    for character in cleartext:
        cyphertext = cyphertext + chr(ord(character)+3)

    return cyphertext

cleartext = "bonjour"
cyphertext = chiffrer_Cesar(cleartext)
print(cyphertext)
    
def déchiffrer_Cesar(cyphertext: str) -> str:
    cleartext =""
    for character in cleartext:
        cleartext = cleartext + chr(ord(character)-3)

    return cleartext

cyphertext = "erqmrxu"
cleartext = déchiffrer_Cesar(cyphertext)
print(cleartext)