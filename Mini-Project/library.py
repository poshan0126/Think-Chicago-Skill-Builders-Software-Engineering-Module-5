from author import AuthorOperations
from book import BookOperations
from genre import GenreOperations
from user import UserOperations

class Library:
    def __init__(self):
        self.book_operations = BookOperations()
        self.user_operations = UserOperations()
        self.author_operations = AuthorOperations()
        self.genre_operations = GenreOperations()

    def add_book(self, book):
        return self.book_operations.add_book(book)

    def borrow_book(self, title, user):
        book = self.book_operations.borrow_book(title)
        if book:
            user.borrow_book(book)
        return book

    def return_book(self, title, user):
        book = self.book_operations.return_book(title)
        if book:
            user.return_book(book)
        return book

    def search_book(self, title):
        return self.book_operations.search_book(title)

    def display_all_books(self):
        return self.book_operations.display_all_books()

    def add_user(self, user):
        return self.user_operations.add_user(user)

    def view_user_details(self, library_id):
        return self.user_operations.view_user_details(library_id)

    def display_all_users(self):
        return self.user_operations.display_all_users()

    def add_author(self, author):
        return self.author_operations.add_author(author)

    def view_author_details(self, name):
        return self.author_operations.view_author_details(name)

    def display_all_authors(self):
        return self.author_operations.display_all_authors()
    def display_books_by_author(self,authorName):
        return self.author_operations.display_books_by_author(authorName)

    def add_genre(self, genre):
        return self.genre_operations.add_genre(genre)

    def view_genre_details(self, name):
        return self.genre_operations.view_genre_details(name)

    def display_all_genres(self):
        return self.genre_operations.display_all_genres()
    def display_books_by_genre(self,genreName):
        return self.genre_operations.display_books_by_genre(genreName)