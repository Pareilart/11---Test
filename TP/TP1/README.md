# TP Tests Unitaires en Python

Ce projet est un exercice d'introduction aux tests unitaires en Python.

## Structure du projet

```
tp_tests/
├── fonctions.py      # Fonctions à tester
├── test_fonctions.py # Tests unitaires
└── README.md        # Ce fichier
```

## Prérequis

- Python 3.6 ou supérieur
- Le module unittest (inclus dans Python)

## Comment exécuter les tests

Pour exécuter les tests, utilisez la commande suivante dans le terminal :

```bash
python test_fonctions.py
```

## Fonctions testées

1. `additionner(a, b)` : Additionne deux nombres
2. `est_pair(nombre)` : Vérifie si un nombre est pair
3. `valider_email(email)` : Valide un email simple
4. `calculer_moyenne(notes)` : Calcule la moyenne d'une liste de notes
5. `convertir_temperature(celsius)` : Convertit des degrés Celsius en Fahrenheit

## Cas de test

Les tests couvrent :
- Cas positifs (entrées valides)
- Cas négatifs (entrées invalides)
- Cas limites (0, liste vide, etc.) 