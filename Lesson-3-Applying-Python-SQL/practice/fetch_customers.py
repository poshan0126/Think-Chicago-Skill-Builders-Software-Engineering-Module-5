import connection_test as ct

conn = ct.connect_database()
def view_database():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM Customers"

            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        finally:
            cursor.close()
            conn.close()
# Task 1.1
def add_view_db():
    if conn is not None:
        try:
            cursor = conn.cursor()
            new_customer = ("K L", "kl@kl.com", "3111111")
            query = "INSERT INTO Customers (name,email,phone) VALUES (%s, %s, %s)"

    

            cursor.execute(query, new_customer)
            conn.commit()
            print("Added Successfully!")
            query = "SELECT * FROM Customers"

            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        finally:
            cursor.close()
            conn.close()

def update_view_db():
    if conn is not None:
        try:
            cursor = conn.cursor()
            update_customer = ("222222", 5)
            query = "UPDATE Customers SET phone = %s WHERE id = %s"

    

            cursor.execute(query, update_customer)
            conn.commit()
            print("Updated Successfully!")
            query = "SELECT * FROM Customers"

            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        finally:
            cursor.close()
            conn.close()

def remove_view_customer():
    if conn is not None:
        try:
            cursor = conn.cursor()
            update_customer = (5,)
            query = "DELETE FROM  Customers WHERE id = %s"

    

            cursor.execute(query, update_customer)
            conn.commit()
            print("Updated Successfully!")
            query = "SELECT * FROM Customers"

            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        finally:
            cursor.close()
            conn.close()
remove_view_customer()