# Cible pour installer les dépendances
install:
	pip install -r requirements.txt
	pip install -e .

# Cible pour lancer les tests
test:
	pytest

# Cible pour la couverture
coverage:
	pytest --cov=src/bibliotheque --cov-report=html

# Cible pour nettoyer
clean:
	rm -rf htmlcov/ .coverage .pytest_cache/ *.egg-info/ build/ dist/

# Cible par défaut
.PHONY: install test coverage clean 