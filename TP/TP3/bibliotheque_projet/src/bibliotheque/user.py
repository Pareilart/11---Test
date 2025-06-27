class User:
    """Représente un utilisateur de la bibliothèque"""

    def __init__(self, name, email):
        """
        Initialise un nouvel utilisateur.
        
        Args:
            name (str): Le nom de l'utilisateur
            email (str): L'adresse email de l'utilisateur (doit contenir @)
            
        Raises:
            ValueError: Si le nom est vide ou si l'email ne contient pas @
        """
        if not name or not name.strip():
            raise ValueError("Le nom ne peut pas être vide")
        if not email or '@' not in email:
            raise ValueError("L'email doit contenir @")

        self.name = name.strip()
        self.email = email
        self.borrowed_books = []

    def can_borrow(self, max_books=3):
        """
        Vérifie si l'utilisateur peut emprunter des livres.
        
        Args:
            max_books (int): Nombre maximum de livres qu'un utilisateur peut emprunter
            
        Returns:
            bool: True si l'utilisateur peut emprunter, False sinon
        """
        return len(self.borrowed_books) < max_books

    def add_borrowed_book(self, book):
        """
        Ajoute un livre à la liste des emprunts de l'utilisateur.
        
        Args:
            book: Le livre à ajouter
            
        Returns:
            bool: True si l'ajout a réussi, False si la limite est atteinte
        """
        if not self.can_borrow():
            return False
        self.borrowed_books.append(book)
        return True

    def remove_borrowed_book(self, book):
        """
        Retire un livre de la liste des emprunts de l'utilisateur.
        
        Args:
            book: Le livre à retirer
            
        Returns:
            bool: True si le retrait a réussi, False si le livre n'était pas emprunté
        """
        if book not in self.borrowed_books:
            return False
        self.borrowed_books.remove(book)
        return True
