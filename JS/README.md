# Projet de Tests Unitaires

Ce projet démontre l'implémentation de tests unitaires en JavaScript en utilisant Jest.

## Structure du Projet

```
.
├── src/
│   ├── discount.js         # Module principal avec la logique de remise
│   └── discount.test.js    # Tests unitaires
├── package.json
└── README.md
```

## Fonctionnalités

Le projet implémente un module de calcul de remise avec deux fonctions principales :
- `calculateDiscount` : Calcule le montant de la remise
- `calculateFinalAmount` : Calcule le montant final après remise

## Tests

Les tests unitaires couvrent les scénarios suivants :
- Calcul de remise avec différents pourcentages (0%, 20%, 100%)
- Gestion des cas d'erreur (montants négatifs, pourcentages invalides)
- Calcul du montant final après remise

### Exécution des Tests

Pour exécuter les tests :
```bash
npm test
```

Pour générer un rapport de couverture :
```bash
npm run test:coverage
```

## Choix Techniques

### Pourquoi Jest ?
- Framework de test moderne et populaire pour JavaScript
- Configuration minimale requise
- Excellente documentation
- Support natif de la couverture de code
- Syntaxe claire et intuitive

### Structure du Code
Le code a été structuré pour être facilement testable en :
- Séparant clairement la logique métier des tests
- Utilisant des fonctions pures (mêmes entrées = mêmes sorties)
- Implémentant une gestion d'erreurs robuste
- Documentant le code avec JSDoc

## Rapports de Test

Les rapports de test générés par Jest incluent :
- Le nombre de tests passés/échoués
- La couverture de code (lignes, branches, fonctions)
- Le temps d'exécution des tests
- Les détails des échecs éventuels 