import pytest
from src.bibliotheque.user import User
from src.bibliotheque.book import Book

class TestUserCreation:
    """Tests de création d'utilisateur"""

    def test_create_valid_user(self):
        """Test création utilisateur valide"""
        user = User("Jean Dupont", "jean.dupont@email.com")
        assert user.name == "Jean Dupont"
        assert user.email == "jean.dupont@email.com"
        assert len(user.borrowed_books) == 0

    def test_create_user_empty_name_raises_error(self):
        """Test nom vide lève une erreur"""
        with pytest.raises(ValueError, match="Le nom ne peut pas être vide"):
            User("", "jean.dupont@email.com")
        
        with pytest.raises(ValueError, match="Le nom ne peut pas être vide"):
            User("   ", "jean.dupont@email.com")

    def test_create_user_invalid_email_raises_error(self):
        """Test email invalide lève une erreur"""
        with pytest.raises(ValueError, match="L'email doit contenir @"):
            User("Jean Dupont", "")

        with pytest.raises(ValueError, match="L'email doit contenir @"):
            User("Jean Dupont", "jean.dupontemail.com")

class TestUserBorrowing:
    """Tests d'emprunt par l'utilisateur"""

    def setup_method(self):
        """Fixture : prépare un utilisateur et des livres pour chaque test"""
        self.user = User("Jean Dupont", "jean.dupont@email.com")
        self.book1 = Book("Le Petit Prince", "Antoine de Saint-Exupéry", "1234567890123")
        self.book2 = Book("1984", "George Orwell", "9876543210123")
        self.book3 = Book("Fahrenheit 451", "Ray Bradbury", "4567890123456")
        self.book4 = Book("Brave New World", "Aldous Huxley", "7890123456789")

    def test_new_user_can_borrow(self):
        """Test nouvel utilisateur peut emprunter"""
        assert self.user.can_borrow() is True
        assert self.user.can_borrow(max_books=5) is True

    def test_user_at_limit_cannot_borrow(self):
        """Test utilisateur à la limite ne peut plus emprunter"""
        # Emprunter 3 livres (limite par défaut)
        self.user.add_borrowed_book(self.book1)
        self.user.add_borrowed_book(self.book2)
        self.user.add_borrowed_book(self.book3)
        
        assert self.user.can_borrow() is False
        assert self.user.can_borrow(max_books=3) is False
        assert self.user.can_borrow(max_books=5) is True

    def test_add_borrowed_book_success(self):
        """Test ajout livre emprunté avec succès"""
        assert self.user.add_borrowed_book(self.book1) is True
        assert len(self.user.borrowed_books) == 1
        assert self.book1 in self.user.borrowed_books

    def test_add_borrowed_book_at_limit_fails(self):
        """Test ajout livre échoue à la limite"""
        # Remplir jusqu'à la limite
        self.user.add_borrowed_book(self.book1)
        self.user.add_borrowed_book(self.book2)
        self.user.add_borrowed_book(self.book3)
        
        # Tenter d'ajouter un 4ème livre
        assert self.user.add_borrowed_book(self.book4) is False
        assert len(self.user.borrowed_books) == 3
        assert self.book4 not in self.user.borrowed_books

    def test_remove_borrowed_book_success(self):
        """Test retrait livre emprunté avec succès"""
        self.user.add_borrowed_book(self.book1)
        assert self.user.remove_borrowed_book(self.book1) is True
        assert len(self.user.borrowed_books) == 0
        assert self.book1 not in self.user.borrowed_books

    def test_remove_not_borrowed_book_fails(self):
        """Test retrait livre non emprunté échoue"""
        assert self.user.remove_borrowed_book(self.book1) is False
