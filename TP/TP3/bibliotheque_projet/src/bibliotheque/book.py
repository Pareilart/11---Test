class Book:
    """Représente un livre dans la bibliothèque"""

    def __init__(self, title, author, isbn):
        """
        Initialise un nouveau livre.
        
        Args:
            title (str): Le titre du livre
            author (str): L'auteur du livre
            isbn (str): Le numéro ISBN du livre (doit avoir 13 caractères)
            
        Raises:
            ValueError: Si le titre ou l'auteur est vide, ou si l'ISBN n'a pas 13 caractères
        """
        if not title or not title.strip():
            raise ValueError("Le titre ne peut pas être vide")
        if not author or not author.strip():
            raise ValueError("L'auteur ne peut pas être vide")
        if not isbn or len(isbn) != 13:
            raise ValueError("L'ISBN doit avoir exactement 13 caractères")

        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn
        self.borrowed = False
        self.current_borrower = None

    def is_available(self):
        """
        Vérifie si le livre est disponible pour l'emprunt.
        
        Returns:
            bool: True si le livre est disponible, False sinon
        """
        return not self.borrowed

    def borrow(self, user):
        """
        Marque le livre comme emprunté.
        
        Args:
            user: L'utilisateur qui emprunte le livre
            
        Returns:
            bool: True si l'emprunt a réussi, False si le livre était déjà emprunté
        """
        if self.borrowed:
            return False
        self.borrowed = True
        self.current_borrower = user
        return True

    def return_book(self):
        """
        Marque le livre comme retourné et disponible.
        
        Returns:
            bool: True si le retour a réussi, False si le livre n'était pas emprunté
        """
        if not self.borrowed:
            return False
        if self.current_borrower:
            self.current_borrower.remove_borrowed_book(self)
            self.current_borrower = None
        self.borrowed = False
        return True
