# 1. Créez "promptmachine.py" qui prend un langage et une question en
# paramètre.
#
# Le script doit s'utiliser comme ceci :
# promptmachine.py python "calculer une moyenne"
# promptmachine.py bash "créer une configuration apache basée sur un template"
#
# Il doit retourner un prompt à envoyer à un chatbot IA et qui permet d'obtenir
# des explications minimales et un maximum d'exemples. 
#
# Le prompt doit être structuré comme ceci:
#
# # Context
# # ...
#
# # Question
# # {question_utilisateur}
# prompt = f'balab ablalal {user_input}'
# promptmachine.py python "calculer une moyenne"

import sys

if len(sys.argv) != 3:
    print("usage: promptmachine.py python 'calculer une moyenne'")
    exit(1)

language = sys.argv[1]
question = sys.argv[2]

allowed_languages = ["python", "bash", "powershell"]
if language not in allowed_languages:
    print("error: only python, bash and powershell are supported")
    exit(1)
# triple """" car on veut imprimer sur plusieurs lignes différentes
print(f"""             
# Context

Tu es un assistant développeur {language}. 
Répond à la question de l'utilisateur uniquement avec un exemple. 
Ton exemple doit être le plus simple possible. 
Ne commente rien, n'explique rien, donne juste du code.

# Question

{question}
""")