import mysql.connector
from book import BookOperations

import database_handler as dbh


mydb = dbh.get_db()
mycursor = mydb.cursor()

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters and setters
    def name(self):
        return self.__name

    def biography(self):
        return self.__biography

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"Biography: {self.__biography}")


class AuthorOperations:
    def __init__(self):
        self.book_operations = BookOperations()

    def add_author(self, author):
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        values = (author.name(), author.biography())
        mycursor.execute(query, values)
        mydb.commit()
        return f"Author '{author.name()}' has been added."

    def view_author_details(self, name):
        query = "SELECT * FROM authors WHERE name = %s"
        mycursor.execute(query, (name,))
        author = mycursor.fetchone()
        if author:
            return str(author)
        else:
            return "Author not found."

    def display_all_authors(self):
        query = "SELECT * FROM authors"
        mycursor.execute(query)
        result = mycursor.fetchall()  # Fetch all rows from the result set
        if result:
            return "\n".join(str(author) for author in result)
        else:
            return "No authors found."

    def display_books_by_author(self, author_name):
        query = "SELECT * FROM books WHERE author = %s"
        mycursor.execute(query, (author_name,))
        books_by_author = mycursor.fetchall()
        if books_by_author:
            return "\n".join(str(book) for book in books_by_author)
        else:
            return f"No books found by author {author_name}."

