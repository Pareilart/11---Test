def capitalize_words(text):
    """Met en majuscule la première lettre de chaque mot."""
    if not isinstance(text, str):
        raise TypeError("L'argument doit être une chaîne")
    return ' '.join(word.capitalize() for word in text.split())

def count_words(text):
    """Compte le nombre de mots."""
    if not isinstance(text, str):
        raise TypeError("L'argument doit être une chaîne")
    return len(text.split()) if text.strip() else 0

def remove_vowels(text):
    """Supprime toutes les voyelles."""
    if not isinstance(text, str):
        raise TypeError("L'argument doit être une chaîne")
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in text if char.lower() not in vowels.lower())
