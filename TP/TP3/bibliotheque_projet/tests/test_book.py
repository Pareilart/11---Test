import pytest
from src.bibliotheque.book import Book
from src.bibliotheque.user import User

class TestBookCreation:
    """Tests de création de livre"""

    def test_create_valid_book(self):
        """Test création livre valide"""
        book = Book("Le Petit Prince", "Antoine de Saint-Exupéry", "1234567890123")
        assert book.title == "Le Petit Prince"
        assert book.author == "Antoine de Saint-Exupéry"
        assert book.isbn == "1234567890123"
        assert not book.borrowed
        assert book.current_borrower is None

    def test_create_book_empty_title_raises_error(self):
        """Test titre vide lève une erreur"""
        with pytest.raises(ValueError, match="Le titre ne peut pas être vide"):
            Book("", "Antoine de Saint-Exupéry", "1234567890123")
        
        with pytest.raises(ValueError, match="Le titre ne peut pas être vide"):
            Book("   ", "Antoine de Saint-Exupéry", "1234567890123")

    def test_create_book_empty_author_raises_error(self):
        """Test auteur vide lève une erreur"""
        with pytest.raises(ValueError, match="L'auteur ne peut pas être vide"):
            Book("Le Petit Prince", "", "1234567890123")
        
        with pytest.raises(ValueError, match="L'auteur ne peut pas être vide"):
            Book("Le Petit Prince", "   ", "1234567890123")

    def test_create_book_invalid_isbn_raises_error(self):
        """Test ISBN invalide lève une erreur"""
        # Test ISBN trop court
        with pytest.raises(ValueError, match="L'ISBN doit avoir exactement 13 caractères"):
            Book("Le Petit Prince", "Antoine de Saint-Exupéry", "12345")

        # Test ISBN trop long
        with pytest.raises(ValueError, match="L'ISBN doit avoir exactement 13 caractères"):
            Book("Le Petit Prince", "Antoine de Saint-Exupéry", "12345678901234")

        # Test ISBN vide
        with pytest.raises(ValueError, match="L'ISBN doit avoir exactement 13 caractères"):
            Book("Le Petit Prince", "Antoine de Saint-Exupéry", "")


class TestBookBorrowing:
    """Tests d'emprunt de livre"""

    def setup_method(self):
        """Fixture : prépare un livre pour chaque test"""
        self.book = Book("Le Petit Prince", "Antoine de Saint-Exupéry", "1234567890123")
        self.user = User("Jean Dupont", "jean.dupont@email.com")

    def test_new_book_is_available(self):
        """Test livre neuf disponible"""
        assert self.book.is_available() is True
        assert self.book.current_borrower is None

    def test_borrow_available_book_success(self):
        """Test emprunt livre disponible"""
        assert self.book.borrow(self.user) is True
        assert self.book.is_available() is False
        assert self.book.current_borrower is self.user

    def test_borrow_already_borrowed_book_fails(self):
        """Test emprunt livre déjà emprunté"""
        # Premier emprunt
        assert self.book.borrow(self.user) is True
        # Tentative de second emprunt
        other_user = User("Marie Martin", "marie.martin@email.com")
        assert self.book.borrow(other_user) is False
        # Le livre reste emprunté par le premier utilisateur
        assert self.book.is_available() is False
        assert self.book.current_borrower is self.user

    def test_return_borrowed_book_success(self):
        """Test retour livre emprunté"""
        self.book.borrow(self.user)
        assert self.book.return_book() is True
        assert self.book.is_available() is True
        assert self.book.current_borrower is None

    def test_return_available_book_fails(self):
        """Test retour livre non emprunté"""
        assert self.book.return_book() is False
        assert self.book.current_borrower is None
