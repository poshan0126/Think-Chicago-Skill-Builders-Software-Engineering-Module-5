from db_handler import connect_database

conn = connect_database("gymdb")
cursor = None
def create_table():
    cursor = conn.cursor()
    try:
        

        # Create the Members table
        cursor.execute('''CREATE TABLE IF NOT EXISTS Members
                    (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, trainer_id INTEGER)''')

        # Create the WorkoutSessions table
        cursor.execute('''CREATE TABLE IF NOT EXISTS WorkoutSessions
(session_id INTEGER PRIMARY KEY AUTO_INCREMENT, member_id INTEGER, date TEXT, duration_minutes INTEGER, calories_burned INTEGER, FOREIGN KEY(member_id) REFERENCES Members(id))''')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
    finally:
        cursor.close()
        conn.close()
# Task 1: Add a Member
def add_member(id, name, age, trainer_id):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Members (id, name, age, trainer_id) VALUES (%s, %s, %s, %s)", (id, name, age, trainer_id))
        conn.commit()
        print(f"Member {name} added successfully.")
        query = "SELECT * FROM Members"

        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
    finally:
        conn.close()

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        cursor.execute("INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)", (member_id, date, duration_minutes, calories_burned))
        conn.commit()
        print("Workout session added successfully.")
        query = "SELECT * FROM WorkoutSessions"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
    finally:
        conn.close()

# Task 3: Update Member Age
def update_member_age(member_id, new_age):
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Members SET age = %s WHERE id = %s", (new_age, member_id))
        if cursor.rowcount == 0:
            print(f"Error: Member with ID {member_id} does not exist.")
        else:
            conn.commit()
            print("Member age updated successfully.")
        query = "SELECT * FROM Members"

        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
    finally:
        conn.close()

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM WorkoutSessions WHERE session_id = %s", (session_id,))
        if cursor.rowcount == 0:
            print(f"Error: Workout session with ID {session_id} does not exist.")
        else:
            conn.commit()
            print("Workout session deleted successfully.")
        query = "SELECT * FROM WorkoutSessions"

        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
    finally:
        conn.close()
# Task 2.1: SQL DISTINCT Usage
def list_distinct_trainers():
    cursor = conn.cursor()
    try:
        query = "SELECT DISTINCT trainer_id FROM Members"
        cursor.execute(query)
        distinct_trainers = [row[0] for row in cursor.fetchall()]
        print("List of distinct trainers:")
        for trainer_id in distinct_trainers:
            print(trainer_id)
    finally:
        conn.close()

# Task 2.2: SQL COUNT Functionality
def count_members_per_trainer():
    cursor = conn.cursor()
    try:
        query = "SELECT trainer_id, COUNT(*) AS member_count FROM Members GROUP BY trainer_id"
        cursor.execute(query)
        results = cursor.fetchall()
        print("Members count per trainer:")
        for row in results:
            trainer_id, member_count = row
            print(f"Trainer ID: {trainer_id}, Member Count: {member_count}")
    finally:
        conn.close()

# Task 3: SQL BETWEEN Usage
def get_members_in_age_range(start_age, end_age):
    cursor = conn.cursor()
    try:
        query = "SELECT name, age, trainer_id FROM Members WHERE age BETWEEN %s AND %s"
        values = (start_age, end_age)
        cursor.execute(query, values)
        members = cursor.fetchall()
        print(f"Members between ages {start_age} and {end_age}:")
        for member in members:
            name, age, trainer_id = member
            print(f"Name: {name}, Age: {age}, Trainer ID: {trainer_id}")
    finally:
        conn.close()


if __name__ == "__main__":
    if conn is not None:
        cursor = conn.cursor()
        # Execute one by one 
        # create_table()
        # add_member('3', 'p p p', "24", "1")
        # add_workout_session( "1", "2024-04-02", "30", "30")
        # update_member_age("1", "26")
        # delete_workout_session("1")
        # list_distinct_trainers()
        # count_members_per_trainer()
        get_members_in_age_range(20, 30)

