# Service de Calcul de Remise

Ce projet implémente un service de calcul de remise en PHP avec Laravel, incluant des tests unitaires.

## Structure du Projet

- `app/Services/DiscountService.php` : Service principal pour le calcul des remises
- `tests/Feature/DiscountTest.php` : Tests unitaires pour le service de remise

## Fonctionnalités

Le service de remise offre deux fonctionnalités principales :

1. `calculateDiscount(float $amount, float $discountPercentage)` : Calcule le montant de la remise
   - Vérifie que le montant n'est pas négatif
   - Vérifie que le pourcentage est entre 0 et 100
   - Retourne le montant de la remise

2. `calculateFinalAmount(float $amount, float $discountPercentage)` : Calcule le montant final après remise
   - Utilise `calculateDiscount` pour obtenir la remise
   - Retourne le montant final après déduction de la remise

## Tests

Les tests unitaires couvrent les scénarios suivants :

- Calcul de remise avec des valeurs valides
- Gestion des montants négatifs
- Gestion des pourcentages invalides
- Calcul du montant final avec différentes remises

### Exécution des Tests

Pour exécuter les tests :

```bash
php artisan test
./vendor/bin/pest --type-coverage
```

## Choix Techniques

- **Laravel** : Framework PHP moderne et robuste
- **PEST** : Framework de test moderne et expressif pour PHP
- **Tests Unitaires** : Approche de test isolée pour garantir la fiabilité du code

## Structure du Code

Le code est structuré pour être :
- Testable : Chaque fonctionnalité peut être testée de manière isolée
- Maintenable : Documentation claire et code bien organisé
- Robuste : Gestion des erreurs et validation des entrées

## Rapports de Test

Les tests génèrent des rapports détaillés incluant :
- Nombre de tests exécutés
- Temps d'exécution
- Assertions réussies
- Gestion des exceptions 