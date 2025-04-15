import re

# Charger le contenu du fichier source
with open('input.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Remplacer les groupes Number;Number;Number; par eux-mêmes suivis d'un \n
modified_content = re.sub(r'(\d+;\d+;\d+;)', r'\1\n', content)

# Sauvegarder le contenu modifié dans un nouveau fichier
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(modified_content)

print("Remplacement terminé. Résultat dans 'output.txt'.")
