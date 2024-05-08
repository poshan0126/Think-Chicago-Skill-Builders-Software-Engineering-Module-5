from library import Library
from book import Book
from author import Author
from genre import Genre
from user import User
import database_handler as dbh

def book_operations_cli(library):
    print("\nBook Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    print("6. Back to Main Menu")

    book_choice = input("\nChoose a book operation: ")

    if book_choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        genre = input("Enter book genre: ")
        publication_date = input("Enter book publication date (YYYY-MM-DD): ")
        book = Book(title, author, isbn, genre, publication_date)
        print(library.add_book(book))

    elif book_choice == '2':
        title = input("Enter book title: ")
        library_id = input("Enter your library ID: ")
        user = library.user_operations.get_user_by_id(library_id)
        if user:
            print(library.borrow_book(title, user))
        else:
            print("User not found.")

    elif book_choice == '3':
        title = input("Enter book title: ")
        library_id = input("Enter your library ID: ")
        user = library.user_operations.get_user_by_id(library_id)
        if user:
            print(library.return_book(title, user))
        else:
            print("User not found.")

    elif book_choice == '4':
        title = input("Enter book title: ")
        print(library.search_book(title))

    elif book_choice == '5':
        print(library.display_all_books())

    elif book_choice == '6':
        return

    else:
        print("Invalid choice. Please choose a valid operation.")

def user_operations_cli(library):
    print("\nUser Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    print("4. Back to Main Menu")

    user_choice = input("\nChoose a user operation: ")

    if user_choice == '1':
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        user = User(name, library_id)
        print(library.add_user(user))

    elif user_choice == '2':
        library_id = input("Enter library ID: ")
        print(library.view_user_details(library_id))

    elif user_choice == '3':
        print(library.display_all_users())

    elif user_choice == '4':
        return

    else:
        print("Invalid choice. Please choose a valid operation.")


def author_operations_cli(library):
    print("\nAuthor Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    print("4. Display book by author")
    print("5. Back to Main Menu")

    author_choice = input("\nChoose an author operation: ")

    if author_choice == '1':
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        author = Author(name, biography)
        print(library.add_author(author))

    elif author_choice == '2':
        name = input("Enter author name: ")
        print(library.view_author_details(name))

    elif author_choice == '3':
        print(library.display_all_authors())
    elif author_choice == '4':
        name = input("Enter author name: ")
        print(library.display_books_by_author(name))

    elif author_choice == '5':
        return

    else:
        print("Invalid choice. Please choose a valid operation.")


def genre_operations_cli(library):
    print("\nGenre Operations:")
    print("1. Add a new genre")
    print("2. View genre details")
    print("3. Display all genres")
    print("4. Display book by genre")
    print("5. Back to Main Menu")

    genre_choice = input("\nChoose a genre operation: ")

    if genre_choice == '1':
        name = input("Enter genre name: ")
        description = input("Enter genre description: ")
        category = input("Enter genre category: ")
        genre = Genre(name, description, category)
        print(library.add_genre(genre))

    elif genre_choice == '2':
        name = input("Enter genre name: ")
        print(library.view_genre_details(name))

    elif genre_choice == '3':
        print(library.display_all_genres())
    
    elif genre_choice == '4':
        name = input("Enter genre name: ")
        print(library.display_books_by_genre(name))

    elif genre_choice == '5':
        return

    else:
        print("Invalid choice. Please choose a valid operation.")
2

def main():
    dbh.create_tables()
    library = Library()

    while True:
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

        choice = input("\nChoose an operation: ")

        if choice == '1':
            book_operations_cli(library)

        elif choice == '2':
            user_operations_cli(library)

        elif choice == '3':
            author_operations_cli(library)

        elif choice == '4':
            genre_operations_cli(library)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    main()