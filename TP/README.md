# Projet de Tests Python

Ce projet contient deux exercices de tests unitaires en Python :
- TP1 : Exercices de base sur les tests unitaires
- TP1C : Exercices avancés sur les tests unitaires avec couverture de code

## Structure du Projet

```
TP/
├── TP1/
│   ├── fonctions.py          # Implémentation des fonctions
│   ├── test_fonctions.py     # Tests unitaires
│   └── README.md            # Documentation spécifique
│
└── TP1C/
    ├── src/                 # Code source
    │   ├── calculator.py
    │   ├── string_utils.py
    │   └── validator.py
    ├── tests/              # Tests unitaires
    │   ├── test_calculator.py
    │   ├── test_string_utils.py
    │   └── test_validator.py
    └── README.md          # Documentation spécifique
```

## Prérequis

- Python 3.9 ou supérieur
- pytest
- pytest-cov (pour la couverture de code)

## Installation

```bash
# Créer un environnement virtuel (optionnel mais recommandé)
python -m venv venv
source venv/bin/activate  # Sur Unix/macOS
# ou
.\venv\Scripts\activate  # Sur Windows

# Installer les dépendances
pip install pytest pytest-cov
```

## Exécution des Tests

### TP1
```bash
cd TP1
python -m pytest test_fonctions.py -v
```

### TP1C
```bash
cd TP1C
python -m pytest tests/ -v
```

Pour voir la couverture de code :
```bash
python -m pytest tests/ --cov=src
```

## Fonctionnalités Testées

### TP1
- Opérations mathématiques de base
- Validation d'email
- Validation de mot de passe
- Conversion de température

### TP1C
- Calculatrice (addition, division, puissance)
- Utilitaires de chaînes de caractères
- Validation d'email et de mot de passe avancée