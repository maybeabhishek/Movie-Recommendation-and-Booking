import sqlite3
db = sqlite3.connect("database.db")
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
    ('Toy Story (1995)', 7),
    ('Jumanji (1995)', 8),
    ('Breakfast Club, The (1985)', 7),
    ('Forrest Gump (1994)', 8),
    ('Pulp Fiction (1994)', 7),
    ('Shawshank Redemption, The (1994)', 7),
    ('Silence of the Lambs, The (1991)', 8),
    ('Star Wars: Episode IV - A New Hope (1977)', 8),
    ('Matrix, The (1999)', 8),
    ('Jurassic Park (1993)', 7),
    ('Braveheart (1995)', 7),
    ('Terminator 2: Judgment Day (1991)', 8),
    ("Schindler's List (1993)", 8),
    ('Fight Club (1999)', 8),
    ('Star Wars: Episode V - The Empire Strikes Back (1980)', 9),
    ('Usual Suspects, The (1995)', 9),
    ('Lord of the Rings: The Fellowship of the Ring, The (2001)', 8),
    ('American Beauty (1999)', 6),
    ('Seven (a.k.a. Se7en) (1995)', 8),
    ('Independence Day (a.k.a. ID4) (1996)', 7),
    ('Apollo 13 (1995)', 7)
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
    (14, '3d', '2018-10-12', '19:00'),
    (15, '3d','2018-10-12', '09:00'),
    (15, '2d', '2018-10-12', '10:00'),
    (16, '3d', '2018-10-12', '08:00'),
    (16, '2d', '2018-10-12', '12:00'),
    (17, '3d', '2018-10-12', '09:00'),
    (18, '2d', '2018-10-12','19:00'),
    (18, '3d', '2018-10-12', '21:00'),
    (18, '2d', '2018-10-01', '22:00'),
    (19, '3d', '2018-10-12', '10:00'),
    (19, '2d', '2018-10-12', '08:00'),
    (19, '2d', '2018-10-12', '12:00'),
    (20, '3d', '2018-10-12', '0900'),
    (20, '3d', '2018-10-12', '19:00'),
    (20, '2d', '2018-10-12', '21:00'),
    (21, '3d', '2018-10-12', '22:00'),
    (21, '2d', '2018-10-12', '10:00'),
    (21, '2d', '2018-10-12', '08:00'),
    (21, '3d', '2018-10-12', '12:00')

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