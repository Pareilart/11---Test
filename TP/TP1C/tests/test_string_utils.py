import pytest
from src.string_utils import capitalize_words, count_words, remove_vowels

class TestStringUtils:
    def test_capitalize_mots_multiples(self):
        assert capitalize_words("hello world") == "Hello World"
        assert capitalize_words("python programming") == "Python Programming"
        assert capitalize_words("TEST CASE") == "Test Case"

    def test_capitalize_type_invalide(self):
        with pytest.raises(TypeError, match="L'argument doit être une chaîne"):
            capitalize_words(123)

    def test_count_words_basique(self):
        assert count_words("hello world python") == 3
        assert count_words("") == 0
        assert count_words("   ") == 0
        assert count_words("single") == 1

    def test_count_words_type_invalide(self):
        with pytest.raises(TypeError, match="L'argument doit être une chaîne"):
            count_words(123)

    def test_remove_vowels_basique(self):
        assert remove_vowels("hello") == "hll"
        assert remove_vowels("python") == "pythn"
        assert remove_vowels("AEIOU") == ""
        assert remove_vowels("bcdfg") == "bcdfg"

    def test_remove_vowels_type_invalide(self):
        with pytest.raises(TypeError, match="L'argument doit être une chaîne"):
            remove_vowels(123)
