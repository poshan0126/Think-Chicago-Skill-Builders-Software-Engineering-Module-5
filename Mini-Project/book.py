import database_handler as dbh


mydb = dbh.get_db()
mycursor = mydb.cursor()


class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availability=True):
        self.title = title  # Define title attribute
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.availability = availability

    # Getters and setters for other attributes...

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.__author}\n"
                f"ISBN: {self.__isbn}\n"
                f"Genre: {self.__genre}\n"
                f"Publication Date: {self.__publication_date}\n"
                f"Availability: {'Available' if self.__availability else 'Unavailable'}")


class BookOperations:
    def __init__(self):
        pass

    def add_book(self, book):
        query = "INSERT INTO books (title, author, isbn, genre, publication_date) VALUES (%s, %s, %s, %s, %s)"
        values = (book.title, book.author, book.isbn, book.genre, book.publication_date)
        mycursor.execute(query, values)
        mydb.commit()
        print(f"Book '{book.title}' has been added to the library.")

    def borrow_book(self, title):
        query = "SELECT * FROM books WHERE title = %s AND availability = 1"
        mycursor.execute(query, (title,))
        book = mycursor.fetchone()
        if book:
            update_query = "UPDATE books SET availability = 0 WHERE id = %s"
            mycursor.execute(update_query, (book[0],))
            mydb.commit()
            return f"You have borrowed '{book[1]}'."
        else:
            return f"The book '{title}' is currently unavailable."

    def return_book(self, title):
        query = "SELECT * FROM books WHERE title = %s AND availability = 0"
        mycursor.execute(query, (title,))
        book = mycursor.fetchone()
        if book:
            update_query = "UPDATE books SET availability = 1 WHERE id = %s"
            mycursor.execute(update_query, (book[0],))
            mydb.commit()
            return f"You have returned '{book[1]}'."
        else:
            return f"The book '{title}' was not borrowed."

    def search_book(self, title):
        query = "SELECT * FROM books WHERE title = %s"
        mycursor.execute(query, (title,))
        book = mycursor.fetchone()
        if book:
            return str(book)
        else:
            return "Book not found."

    def display_all_books(self):
        query = "SELECT * FROM books"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if result:
            return "\n".join(str(book) for book in result)
        else:
            return "No books found."
