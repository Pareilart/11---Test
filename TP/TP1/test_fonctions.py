import pytest
from fonctions import additionner, est_pair, valider_email, calculer_moyenne, convertir_temperature, diviser, valider_mot_de_passe

def test_additionner():
    # Test des cas valides
    assert additionner(2, 3) == 5
    assert additionner(-2, -3) == -5
    assert additionner(2.5, 3.5) == 6.0
    
    # Test des raises
    with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
        additionner("2", 3)
    with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
        additionner(2, "3")

def test_est_pair():
    # Test des cas valides
    assert est_pair(2) is True
    assert est_pair(3) is False
    assert est_pair(0) is True
    
    # Test des raises
    with pytest.raises(TypeError, match="L'argument doit être un entier"):
        est_pair(2.5)
    with pytest.raises(TypeError, match="L'argument doit être un entier"):
        est_pair("2")

def test_valider_email():
    # Test des cas valides
    assert valider_email("test@example.com") is True
    assert valider_email("invalid") is False
    assert valider_email("testexample.com") is False
    assert valider_email("test@example") is False
    
    # Test des raises
    with pytest.raises(TypeError, match="L'email doit être une chaîne de caractères"):
        valider_email(123)

def test_calculer_moyenne():
    # Test des cas valides
    assert calculer_moyenne([1, 2, 3]) == 2
    assert calculer_moyenne([]) == 0
    assert calculer_moyenne([18]) == 18
    assert calculer_moyenne([10, 15, 20]) == 15
    
    # Test des raises
    with pytest.raises(TypeError, match="L'argument doit être une liste"):
        calculer_moyenne("1,2,3")
    with pytest.raises(TypeError, match="Toutes les notes doivent être des nombres"):
        calculer_moyenne([1, "2", 3])

def test_convertir_temperature():
    # Test des cas valides
    assert convertir_temperature(0) == 32
    assert convertir_temperature(100) == 212
    
    # Test des raises
    with pytest.raises(TypeError, match="La température doit être un nombre"):
        convertir_temperature("0")

def test_diviser():
    # Test des cas valides
    assert diviser(6, 2) == 3
    assert diviser(5, 2) == 2.5
    assert diviser(10, 2) == 5
    
    # Test des raises
    with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
        diviser("6", 2)
    with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
        diviser(6, "2")
    with pytest.raises(ValueError, match="Division par zéro impossible"):
        diviser(6, 0)

def test_valider_mot_de_passe():
    # Test des cas valides
    assert valider_mot_de_passe("Test123!@") is True
    assert valider_mot_de_passe("Test1!") is False  # trop court
    assert valider_mot_de_passe("test123!@") is False  # sans majuscule
    assert valider_mot_de_passe("TEST123!@") is False  # sans minuscule
    assert valider_mot_de_passe("TestTest!@") is False  # sans chiffre
    assert valider_mot_de_passe("Test1234") is False  # sans caractère spécial
    
    # Test des raises
    with pytest.raises(TypeError, match="Le mot de passe doit être une chaîne de caractères"):
        valider_mot_de_passe(123) 