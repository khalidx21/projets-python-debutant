# ⏳ 03 - Minuteur / Compte à rebours

## 🎯 Objectif

- Apprendre à utiliser les boucles avec `time.sleep()` pour créer une pause dans l'exécution du programme.

## 📝 Description

Le programme demande un nombre de secondes, puis affiche un compte à rebours jusqu'à 0, en marquant une pause d'une seconde entre chaque nombre.

**Exemple d'entrée :**
- Secondes : `5`

**Sortie attendue :**
```
5
4
3
2
1
Fin !
```

## ✨ Concepts clés

- `time.sleep(1)` pour faire une pause d'une seconde.
- Boucle `while` ou `for` pour décrémenter le temps.
- `int()` pour convertir l'entrée en nombre entier.
- `print()` pour afficher le temps restant.

## 🚀 Extensions possibles

- Jouer un son (bip) à la fin du compte à rebours.
- Permettre à l'utilisateur de choisir une durée en minutes et secondes.
- Afficher le temps restant dans un format plus lisible (ex: `mm:ss`).
- Créer une version visuelle simple dans le terminal (ex: une barre de progression).

## 📚 Ressources utiles

- [Documentation du module `time`](https://docs.python.org/fr/3/library/time.html)