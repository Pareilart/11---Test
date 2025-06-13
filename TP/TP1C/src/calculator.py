def add(a, b):
    """
    Additionne deux nombres.

    Raises:
        TypeError: Si un argument n'est pas un nombre
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres")
    return a + b

def divide(a, b):
    """
    Divise a par b.

    Returns:
        float: Quotient (toujours en float)

    Raises:
        TypeError: Si un argument n'est pas un nombre
        ZeroDivisionError: Si b est égal à 0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres")
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible")
    return float(a / b)

def power(base, exponent):
    """
    Calcule base^exponent.

    Raises:
        ValueError: Si base=0 et exponent<0
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Les arguments doivent être des nombres")
    if base == 0 and exponent < 0:
        raise ValueError("0 ne peut pas être élevé à une puissance négative")
    return base ** exponent
