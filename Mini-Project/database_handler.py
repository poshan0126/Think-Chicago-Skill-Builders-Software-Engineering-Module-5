import mysql.connector

def create_tables():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0715",
        database="library_management_system"
    )

    mycursor = mydb.cursor()

    # Create books table
    mycursor.execute("CREATE TABLE IF NOT EXISTS books ("
                     "id INT AUTO_INCREMENT PRIMARY KEY,"
                     "title VARCHAR(255) NOT NULL,"
                     "author VARCHAR(255) NOT NULL,"
                     "isbn VARCHAR(13) NOT NULL,"
                     "genre VARCHAR(255) NOT NULL,"
                     "publication_date DATE NOT NULL,"
                     "availability BOOLEAN DEFAULT 1"
                     ")")

    # Create authors table

    mycursor.execute("CREATE TABLE IF NOT EXISTS authors ("
                     "id INT AUTO_INCREMENT PRIMARY KEY,"
                     "name VARCHAR(255) NOT NULL,"
                     "biography TEXT"
                     ")")

    # Create genres table
    mycursor.execute("CREATE TABLE IF NOT EXISTS genres ("
                     "id INT AUTO_INCREMENT PRIMARY KEY,"
                     "name VARCHAR(255) NOT NULL,"
                     "description TEXT,"
                     "category VARCHAR(50)"
                     ")")

    # Create users table
    mycursor.execute("CREATE TABLE IF NOT EXISTS users ("
                     "id INT AUTO_INCREMENT PRIMARY KEY,"
                     "name VARCHAR(255) NOT NULL,"
                     "library_id VARCHAR(10) NOT NULL UNIQUE"
                     ")")

    # Create borrowed_books table
    mycursor.execute("CREATE TABLE IF NOT EXISTS borrowed_books ("
                     "id INT AUTO_INCREMENT PRIMARY KEY,"
                     "user_id INT,"
                     "book_id INT,"
                     "borrow_date DATE NOT NULL,"
                     "return_date DATE,"
                     "FOREIGN KEY (user_id) REFERENCES users(id),"
                     "FOREIGN KEY (book_id) REFERENCES books(id)"
                     ")")
def get_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0715",
        database="library_management_system"
    )
    return mydb

if __name__ == "__main__":
    create_tables()
