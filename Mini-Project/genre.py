import mysql.connector
from book import BookOperations


import database_handler as dbh


mydb = dbh.get_db()
mycursor = mydb.cursor()

class Genre:
    def __init__(self, name, description, category):
        self.name = name  # Define name attribute
        self.description = description
        self.category = category

    # Getters and setters for other attributes...

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Description: {self.__description}\n"
                f"Category: {self.__category}")


class GenreOperations:
    def __init__(self):
        self.book_operations = BookOperations()

    def add_genre(self, genre):
        query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
        values = (genre.name, genre.description, genre.category)
        mycursor.execute(query, values)
        mydb.commit()
        return f"Genre '{genre.name}' has been added."

    def view_genre_details(self, name):
        query = "SELECT * FROM genres WHERE name = %s"
        mycursor.execute(query, (name,))
        genre = mycursor.fetchone()
        if genre:
            return str(genre)
        else:
            return "Genre not found."

    def display_all_genres(self):
        query = "SELECT * FROM genres"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if result:
            return "\n".join(str(genre) for genre in result)
        else:
            return "No genres found."

    def display_books_by_genre(self, genre_name):
        query = "SELECT * FROM books WHERE genre = %s"
        mycursor.execute(query, (genre_name,))
        books_by_genre = mycursor.fetchall()
        if books_by_genre:
            return "\n".join(str(book) for book in books_by_genre)
        else:
            return f"No books found in genre {genre_name}."
