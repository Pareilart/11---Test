import pytest
from src.bibliotheque.library import Library
from src.bibliotheque.book import Book
from src.bibliotheque.user import User

class TestLibrary:
    """Tests de la bibliothèque"""

    def setup_method(self):
        """Fixture : prépare une bibliothèque pour chaque test"""
        self.library = Library("Bibliothèque Municipale")
        self.book = Book("Le Petit Prince", "Antoine de Saint-Exupéry", "1234567890123")
        self.user = User("Jean Dupont", "jean.dupont@email.com")

    def test_library_creation(self):
        """Test création bibliothèque"""
        assert self.library.name == "Bibliothèque Municipale"
        assert len(self.library.books) == 0
        assert len(self.library.users) == 0

    def test_add_book_success(self):
        """Test ajout livre avec succès"""
        assert self.library.add_book(self.book) is True
        assert len(self.library.books) == 1
        assert self.library.books[0] is self.book

    def test_add_duplicate_book_fails(self):
        """Test ajout livre doublon échoue"""
        self.library.add_book(self.book)
        duplicate_book = Book("Le Petit Prince 2", "Antoine de Saint-Exupéry", "1234567890123")
        assert self.library.add_book(duplicate_book) is False
        assert len(self.library.books) == 1

    def test_find_book_by_isbn_success(self):
        """Test recherche livre par ISBN avec succès"""
        self.library.add_book(self.book)
        found_book = self.library.find_book_by_isbn("1234567890123")
        assert found_book is self.book

    def test_find_book_by_isbn_not_found(self):
        """Test recherche livre par ISBN non trouvé"""
        found_book = self.library.find_book_by_isbn("9999999999999")
        assert found_book is None

    def test_borrow_book_success(self):
        """Test emprunt livre avec succès"""
        self.library.add_book(self.book)
        assert self.library.borrow_book(self.user, "1234567890123") is True
        assert not self.book.is_available()
        assert self.book in self.user.borrowed_books
        assert self.book.current_borrower is self.user

    def test_borrow_nonexistent_book_fails(self):
        """Test emprunt livre inexistant échoue"""
        assert self.library.borrow_book(self.user, "9999999999999") is False

    def test_borrow_unavailable_book_fails(self):
        """Test emprunt livre indisponible échoue"""
        self.library.add_book(self.book)
        other_user = User("Marie Martin", "marie.martin@email.com")
        
        # Premier emprunt réussi
        assert self.library.borrow_book(self.user, "1234567890123") is True
        
        # Deuxième emprunt échoue
        assert self.library.borrow_book(other_user, "1234567890123") is False

    def test_borrow_exceeding_limit_fails(self):
        """Test emprunt dépassant limite échoue"""
        # Créer et ajouter 3 livres
        books = [
            self.book,
            Book("1984", "George Orwell", "9876543210123"),
            Book("Fahrenheit 451", "Ray Bradbury", "4567890123456")
        ]
        for book in books:
            self.library.add_book(book)
            self.library.borrow_book(self.user, book.isbn)

        # Tenter d'emprunter un 4ème livre
        fourth_book = Book("Brave New World", "Aldous Huxley", "7890123456789")
        self.library.add_book(fourth_book)
        assert self.library.borrow_book(self.user, "7890123456789") is False

    def test_borrow_and_return_book_cycle(self):
        """Test cycle complet d'emprunt et retour"""
        self.library.add_book(self.book)
        
        # Emprunt réussi
        assert self.library.borrow_book(self.user, "1234567890123") is True
        assert not self.book.is_available()
        assert self.book in self.user.borrowed_books
        assert self.book.current_borrower is self.user
        
        # Retour réussi
        assert self.book.return_book() is True
        assert self.book.is_available()
        assert self.book not in self.user.borrowed_books
        assert self.book.current_borrower is None
