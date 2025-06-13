import pytest
from src.validator import is_valid_email, validate_password_strength

class TestEmailValidation:
    def test_emails_valides(self):
        valides = [
            "user@example.com",
            "test.email@domain.org",
            "user.name@domain.co.uk",
            "user-name@domain.com",
            "user123@domain.com"
        ]
        for email in valides:
            assert is_valid_email(email) == True

    def test_emails_invalides(self):
        invalides = [
            "user",
            "user@",
            "@domain.com",
            "user@domain",
            "user@.com",
            "user@domain.",
            "user@domain.c",
            "user@domain.comm",
            "user name@domain.com",
            "user@domain name.com"
        ]
        for email in invalides:
            assert is_valid_email(email) == False

    def test_type_invalide(self):
        with pytest.raises(TypeError, match="L'email doit être une chaîne"):
            is_valid_email(123)

class TestPasswordStrength:
    def test_password_fort(self):
        result = validate_password_strength("MyStrong123!")
        assert result['is_valid'] == True
        assert result['score'] >= 4
        assert len(result['missing_criteria']) == 0

    def test_password_faible(self):
        result = validate_password_strength("weak")
        assert result['is_valid'] == False
        assert result['score'] < 4
        assert len(result['missing_criteria']) > 0

    def test_password_critères_manquants(self):
        result = validate_password_strength("password")
        assert result['is_valid'] == False
        assert 'majuscule' in result['missing_criteria']
        assert 'chiffre' in result['missing_criteria']
        assert 'special' in result['missing_criteria']

    def test_type_invalide(self):
        with pytest.raises(TypeError, match="Le mot de passe doit être une chaîne"):
            validate_password_strength(123)
