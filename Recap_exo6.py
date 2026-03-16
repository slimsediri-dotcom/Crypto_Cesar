# Crée un dictionnaire associant des pays à leurs capitales.
# Étant donné un pays, affiche sa capitale.

# https://www.w3schools.com/python/python_dictionaries.asp

# Créer le dictionnaire, pays=clé, capitale = valeur
dictionnaire_capitales = {"brésil":"brasilia", "belgique":"bruxelles", "japon":"tokyo"} 

# Stocke dans une variable le pays dont je veux la capitale
country = "brésil" 

# Python recherche la variable country (il trouve "brésil")
# Il va dans le dictionnaire annuaire_capitales et cherche l'étiquette "brésil"
# Il toruve la valeur associée ("brasilia") et la range dans la nouvelle variable capitale
capitale = dictionnaire_capitales[country]
print(f"La capitale du {country} est {'brasilia'}")
