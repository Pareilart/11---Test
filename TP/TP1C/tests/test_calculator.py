import pytest
from src.calculator import add, divide, power

class TestAddition:
    def test_add_integers(self):
        assert add(5, 3) == 8

    def test_add_floats(self):
        assert add(2.5, 3.7) == pytest.approx(6.2)

    def test_add_avec_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5

    def test_add_negatifs(self):
        assert add(-5, -3) == -8
        assert add(10, -7) == 3

    def test_add_type_invalide(self):
        with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
            add("5", 3)
        with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
            add(5, "3")

class TestDivision:
    def test_divide_entiers(self):
        assert divide(10, 2) == 5.0

    def test_divide_decimal(self):
        assert divide(7, 3) == pytest.approx(2.333333)

    def test_divide_par_zero(self):
        with pytest.raises(ZeroDivisionError, match="Division par zéro impossible"):
            divide(10, 0)

    def test_divide_zero_dividende(self):
        assert divide(0, 5) == 0.0

    def test_divide_type_invalide(self):
        with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
            divide("10", 2)
        with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
            divide(10, "2")

class TestPower:
    def test_power_basique(self):
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_exposant_zero(self):
        assert power(5, 0) == 1
        assert power(0, 0) == 1

    def test_power_zero_exposant_negatif(self):
        with pytest.raises(ValueError, match="0 ne peut pas être élevé à une puissance négative"):
            power(0, -1)

    def test_power_type_invalide(self):
        with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
            power("2", 3)
        with pytest.raises(TypeError, match="Les arguments doivent être des nombres"):
            power(2, "3")
