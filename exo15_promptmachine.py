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

import sys
sys.argv.pop(0)

language_list = ["java", "python", "ruby", "php", "C++"]
language = sys.argv[0]   #accéder à l'indice 0
question = []

#context
if language not in language_list:
    print("usage: program_name language question")
    print("le langage doit être un des langages suivants: java, python, ruby, php, C++")
    exit(1)
print(f"Je suis un développeur {language} expérimenté et je souhaite une réponse la plus simple possible, uniquement du code, à ma question.") 

#question 
sys.argv.pop(0)
for arg in sys.argv:
    question.append(arg)
if not 4 <= len(question) < 200:
    print("la question est trop courte ou trop longue, merci de reformuler plus succintement, min 4 mots, max. 200 mots")
ma_question = " ".join(question) # concaténer, et transformer en une chaîne, les caractères de la liste question
print(ma_question)
# code ok mais un peu trop compliqué, 
# 1) j'aurais pu passer language sys.argv[1] et en sys.argv[2]
# 2) rentrer mon trpoisième argument, ma question, en une chaine de caractère "question" 