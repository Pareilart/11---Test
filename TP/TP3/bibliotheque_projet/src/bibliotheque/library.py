from .book import Book
from .user import User

class Library:
    """Gestionnaire de bibliothèque"""

    def __init__(self, name):
        """
        Initialise une nouvelle bibliothèque.
        
        Args:
            name (str): Le nom de la bibliothèque
        """
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        """
        Ajoute un livre à la collection.
        
        Args:
            book (Book): Le livre à ajouter
            
        Returns:
            bool: True si l'ajout a réussi, False si le livre existe déjà
        """
        if any(b.isbn == book.isbn for b in self.books):
            return False
        self.books.append(book)
        return True

    def find_book_by_isbn(self, isbn):
        """
        Trouve un livre par son ISBN.
        
        Args:
            isbn (str): L'ISBN du livre recherché
            
        Returns:
            Book: Le livre trouvé ou None si non trouvé
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def borrow_book(self, user, isbn):
        """
        Gère l'emprunt d'un livre par un utilisateur.
        
        Args:
            user (User): L'utilisateur qui emprunte
            isbn (str): L'ISBN du livre à emprunter
            
        Returns:
            bool: True si l'emprunt a réussi, False sinon
        """
        # 1. Trouver le livre
        book = self.find_book_by_isbn(isbn)
        if not book:
            return False

        # 2. Vérifier que l'utilisateur peut emprunter
        if not user.can_borrow():
            return False

        # 3. Vérifier que le livre est disponible
        if not book.is_available():
            return False

        # 4. Effectuer l'emprunt
        if book.borrow(user) and user.add_borrowed_book(book):
            return True

        # En cas d'échec, annuler les changements
        book.return_book()
        user.remove_borrowed_book(book)
        return False
