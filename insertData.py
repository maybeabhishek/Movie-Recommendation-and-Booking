import sqlite3
db = sqlite3.connect("movie_db.db")
cursor = db.cursor()

# Create tables
create_movies_table = """
CREATE TABLE IF NOT EXISTS
Movies(id INTEGER PRIMARY KEY, movie_name TEXT, movie_rating FLOAT)
"""
cursor.execute(create_movies_table)

create_projections_table = """
CREATE TABLE IF NOT EXISTS
Projections(id INTEGER PRIMARY KEY, movie_id INTEGER, projection_type TEXT,
projection_date TEXT, projection_time TEXT,
FOREIGN KEY (movie_id) REFERENCES Movies(id))
"""
cursor.execute(create_projections_table)

create_reservations_table = """
CREATE TABLE IF NOT EXISTS
Reservations(id INTEGER PRIMARY KEY, username TEXT,
projection_id INTEGER, row INTEGER, col INTEGER,
FOREIGN KEY (projection_id) REFERENCES Projections(id))
"""
cursor.execute(create_reservations_table)
db.commit()

# Insert Movies
movies = [
    ('Venom', 7),
    ('Iron Man', 8),
    ('Spider-Man', 7),
    ('Black panther', 8),
    ('Harry potter and the chamber of secrets', 7),
    ('Greatest showman', 7),
    ('La la land', 8),
    ('Titanic', 8),
    ('The Avengers', 8),
    ('Avengers age of ultron', 7),
    ('Thor', 7),
    ('Batman Arkham knight', 8),
    ('Flash', 8),
    ('Justice League', 6)
]

cursor.executemany(""" INSERT INTO Movies(
movie_name, movie_rating) VALUES(?,?)
""", movies)
db.commit()

# Insert Projections
projections = [
    (1, '3d','2018-10-12', '09:00'),
    (1, '2d', '2018-10-12', '10:00'),
    (2, '3d', '2018-10-12', '08:00'),
    (2, '2d', '2018-10-12', '12:00'),
    (3, '3d', '2018-10-12', '09:00'),
    (4, '2d', '2018-10-12','19:00'),
    (5, '3d', '2018-10-12', '21:00'),
    (6, '2d', '2018-10-01', '22:00'),
    (6, '3d', '2018-10-12', '10:00'),
    (7, '2d', '2018-10-12', '08:00'),
    (8, '2d', '2018-10-12', '12:00'),
    (8, '3d', '2018-10-12', '0900'),
    (9, '3d', '2018-10-12', '19:00'),
    (10, '2d', '2018-10-12', '21:00'),
    (11, '3d', '2018-10-12', '22:00'),
    (12, '2d', '2018-10-12', '10:00'),
    (13, '2d', '2018-10-12', '08:00'),
    (13, '3d', '2018-10-12', '12:00'),
    (14, '3d', '2018-10-12', '09:00'),
    (14, '3d', '2018-10-12', '19:00')

]
cursor.executemany(""" INSERT INTO Projections(
movie_id, projection_type, projection_date, projection_time) VALUES(?,?,?,?)
""", projections)
db.commit()

# Insert Reservations
reservations = [
    ("Neil Patrick", 1, 2, 1),
    ("Armstrong", 1, 3, 5),
    ("Ronaldo", 1, 7, 8),
    ("50 Cent", 3, 1, 1),
    ("Pop", 3, 1, 2),
    ("Entity", 5, 2, 3),
    ("Son", 5, 2, 4)
]

cursor.executemany(""" INSERT INTO Reservations(
username, projection_id, row, col) VALUES(?,?,?,?)
""", reservations)
db.commit()