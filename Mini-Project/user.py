import mysql.connector
import database_handler as dbh


mydb = dbh.get_db()
mycursor = mydb.cursor()

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    # Getters and setters

    def borrow_book(self, book):
        self.__borrowed_books.append(book)
        return f"User '{self.__name}' has borrowed the book '{book.title}'."

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            return f"User '{self.__name}' has returned the book '{book.title}'."
        else:
            return f"User '{self.__name}' did not borrow the book '{book.title}'."

    def __str__(self):
        borrowed_book_titles = "\n".join(str(book) for book in self.__borrowed_books)
        return (f"Name: {self.__name}\n"
                f"Library ID: {self.__library_id}\n"
                f"Borrowed Books: {borrowed_book_titles}")

class UserOperations:
    def __init__(self):
        pass

    def add_user(self, user):
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        values = (user.name, user.library_id)
        mycursor.execute(query, values)
        mydb.commit()
        return f"User '{user.name}' has been added."

    def get_user_by_id(self, library_id):
        query = "SELECT * FROM users WHERE library_id = %s"
        mycursor.execute(query, (library_id,))
        user = mycursor.fetchone()
        if user:
            return User(user[1], user[2])
        else:
            print("No user found with the given library ID.")
            return None

    def view_user_details(self, library_id):
        query = "SELECT * FROM users WHERE library_id = %s"
        mycursor.execute(query, (library_id,))
        user = mycursor.fetchone()
        if user:
            return f"Name: {user[1]}\nLibrary ID: {user[2]}"
        else:
            return "User not found."

    def display_all_users(self):
        query = "SELECT * FROM users"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if result:
            return "\n".join(f"Name: {user[1]}\nLibrary ID: {user[2]}" for user in result)
        else:
            return "No users found."
