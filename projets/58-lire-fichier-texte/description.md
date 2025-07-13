# 📄 58 - Lecteur de fichier texte

## 🎯 Objectif

- Ouvrir et lire le contenu d'un fichier texte ligne par ligne.

## 📝 Description

Le programme ouvre un fichier `exemple.txt` (que vous devez créer), lit son contenu ligne par ligne, et affiche chaque ligne avec son numéro.

## ✨ Concepts clés

- `with open(...)` en mode lecture (`'r'`).
- Itérer sur un objet fichier avec une boucle `for`.
- Utiliser `enumerate()` pour obtenir le numéro de ligne.

## 🚀 Extensions possibles

- Permettre à l'utilisateur de spécifier le nom du fichier à lire.
- Gérer les erreurs si le fichier n'existe pas (`FileNotFoundError`).
- Compter le nombre de lignes et de mots dans le fichier.

## 📚 Ressources utiles

- [Lecture de fichiers en Python](https://www.w3schools.com/python/python_file_open.asp)