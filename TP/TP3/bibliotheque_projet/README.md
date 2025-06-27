# Projet Bibliothèque

Ce projet implémente un système simple de gestion de bibliothèque en Python, permettant la gestion des livres, des utilisateurs et des emprunts.

## Installation

1. Clonez le dépôt :
```bash
git clone <url-du-depot>
cd bibliotheque_projet
```

2. Créez un environnement virtuel (recommandé) :
```bash
python -m venv venv
source venv/bin/activate  # Sur Unix/macOS
# ou
venv\Scripts\activate  # Sur Windows
```

3. Installez les dépendances :
```bash
make install
# ou
pip install -r requirements.txt
```

## Tests

### Lancer les tests

Plusieurs options sont disponibles :

1. Lancer tous les tests :
```bash
make test
# ou
pytest
```

2. Lancer les tests avec plus de détails :
```bash
pytest -v
```

3. Lancer les tests d'un fichier spécifique :
```bash
pytest tests/test_book.py
```

4. Lancer un test spécifique :
```bash
pytest tests/test_book.py::TestBookCreation::test_create_valid_book
```

### Couverture des tests

Pour générer un rapport de couverture :

1. Rapport dans le terminal :
```bash
pytest --cov=src/bibliotheque
```

2. Rapport HTML détaillé :
```bash
make coverage
# ou
pytest --cov=src/bibliotheque --cov-report=html
```

Le rapport HTML sera généré dans le dossier `htmlcov/`. Ouvrez `htmlcov/index.html` dans votre navigateur pour le consulter.

## Structure du projet

```
bibliotheque_projet/
├── src/
│   └── bibliotheque/
│       ├── book.py         # Gestion des livres
│       ├── user.py         # Gestion des utilisateurs
│       └── library.py      # Gestion de la bibliothèque
├── tests/
│   ├── test_book.py       # Tests des livres
│   ├── test_user.py       # Tests des utilisateurs
│   └── test_library.py    # Tests de la bibliothèque
├── pytest.ini             # Configuration pytest
├── requirements.txt       # Dépendances
└── Makefile              # Automatisation des tâches
```

## Fonctionnalités

- Gestion des livres (ajout, recherche par ISBN)
- Gestion des utilisateurs (création, validation)
- Système d'emprunt avec limites
- Validation des données (ISBN, email, etc.)

## Développement

### Commandes utiles

- `make clean` : Nettoie les fichiers temporaires
- `make test` : Lance les tests
- `make coverage` : Génère le rapport de couverture

### Bonnes pratiques

- Écrire des tests pour chaque nouvelle fonctionnalité
- Maintenir une couverture de tests > 90%
- Suivre les conventions de nommage Python (PEP 8)
- Documenter les classes et méthodes avec des docstrings
