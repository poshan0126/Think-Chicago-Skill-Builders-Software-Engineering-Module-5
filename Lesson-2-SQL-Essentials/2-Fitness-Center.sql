CREATE DATABASE FitnessCenter;
USE FitnessCenter;

CREATE TABLE Trainers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    expertise VARCHAR(100)
);

CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    trainer_id INT,
    FOREIGN KEY (trainer_id) REFERENCES Trainers(id)
);
CREATE TABLE WorkoutSessions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT NOT NULL,
    session_time VARCHAR(20) NOT NULL,
    workout_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Members(id)
);
-- Task 1
-- Insert new trainers into the Trainers table
INSERT INTO Trainers (id, name, expertise)
VALUES
    (1, 'Trainer1', 'flex'),
    (2, 'Trainer2', 'flex'),
    (3, 'Trainer3', 'flex'),
    (4, 'Trainer4', 'flex');
-- Insert new members into the Members table
INSERT INTO Members (id, name, age, trainer_id)
VALUES
    (1, 'Member 1', 32, 1),
    (2, 'Member 2', 28, 2),
    (3, 'Member 3', 45, 3),
    (4, 'Member 4', 21, 4);

-- Insert workout session details into the WorkoutSessions table
INSERT INTO WorkoutSessions (member_id, session_time, workout_type)
VALUES
    (1, 'Morning', 'Strength Training'),
    (2, 'Evening', 'Cardio'),
    (3, 'Afternoon', 'Yoga'),
    (4, 'Morning', 'HIIT');
    
    -- Task 2
    -- Update the workout session time for Member 1
UPDATE WorkoutSessions
SET session_time = 'Evening'
WHERE member_id = (
    SELECT id
    FROM Members
    WHERE name = 'Member 1'
);

SELECT * FROM WorkoutSessions;
SELECT * FROM Members;
-- Task 3
-- Delete the record for Member 4 from the Members table
DELETE FROM WorkoutSessions
WHERE member_id = (
    SELECT id
    FROM Members
    WHERE name = 'Member 4'
);

DELETE FROM Members
WHERE name = 'Member 4';
SELECT * FROM Members;

