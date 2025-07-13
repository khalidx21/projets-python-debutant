# 🔐 25 - Password Locker

## 🎯 Objectif

- Créer un gestionnaire de mots de passe simple qui stocke les données dans un dictionnaire et les sauvegarde (de manière non sécurisée) dans un fichier.

## 📝 Description

Le programme permet à l'utilisateur de sauvegarder des mots de passe pour différents services (par exemple, email, facebook, etc.). Il peut ajouter de nouvelles entrées et consulter les mots de passe existants.

**Note :** Ce projet est à des fins éducatives et n'est **pas sécurisé**. Ne l'utilisez pas pour de vrais mots de passe.

## ✨ Concepts clés

- Dictionnaires pour stocker les paires service/mot de passe.
- Sérialisation avec `json` ou `pickle` pour sauvegarder le dictionnaire dans un fichier.
- Menus en console pour interagir avec l'utilisateur.

## 🚀 Extensions possibles

- Ajouter une fonction pour supprimer des entrées.
- Mettre en place un mot de passe principal pour accéder au programme (toujours non sécurisé, mais une bonne pratique à apprendre).
- Copier un mot de passe dans le presse-papiers.

## 📚 Ressources utiles

- [Module `json` en Python](https://docs.python.org/3/library/json.html)