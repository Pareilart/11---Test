import re

def is_valid_email(email):
    """Valide une adresse email."""
    if not isinstance(email, str):
        raise TypeError("L'email doit être une chaîne")

    if email.count('@') != 1:
        return False

    local_part, domain = email.split('@')
    
    # Validation de la partie locale
    if not re.match(r'^[a-zA-Z0-9._-]+$', local_part):
        return False
    if len(local_part) < 1 or len(local_part) > 64:
        return False

    # Validation du domaine
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    
    # Vérification de l'extension
    extension = domain_parts[-1]
    if not re.match(r'^[a-zA-Z]{2,3}$', extension):
        return False

    # Vérification du reste du domaine
    domain_without_extension = '.'.join(domain_parts[:-1])
    if not re.match(r'^[a-zA-Z0-9.-]+$', domain_without_extension):
        return False

    return True

def validate_password_strength(password):
    """Évalue la force d'un mot de passe."""
    if not isinstance(password, str):
        raise TypeError("Le mot de passe doit être une chaîne")

    result = {
        'is_valid': False,
        'score': 0,
        'missing_criteria': []
    }

    # Critères de validation
    criteria = {
        'longueur': lambda p: len(p) >= 8,
        'majuscule': lambda p: any(c.isupper() for c in p),
        'minuscule': lambda p: any(c.islower() for c in p),
        'chiffre': lambda p: any(c.isdigit() for c in p),
        'special': lambda p: any(c in '!@#$%^&*' for c in p)
    }

    # Vérification de chaque critère
    for name, check in criteria.items():
        if check(password):
            result['score'] += 1
        else:
            result['missing_criteria'].append(name)

    result['is_valid'] = result['score'] >= 4
    return result
