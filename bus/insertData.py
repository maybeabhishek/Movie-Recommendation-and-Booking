import sqlite3
db = sqlite3.connect("travel_db.db")
cursor = db.cursor()

# Create tables
create_travel_table = """
CREATE TABLE IF NOT EXISTS
travels(id INTEGER PRIMARY KEY, travel_name TEXT, travel_rating FLOAT)
"""
cursor.execute(create_travel_table)

create_journey_table = """
CREATE TABLE IF NOT EXISTS
Journey(id INTEGER PRIMARY KEY, travel_id INTEGER, tour_name TEXT,
journey_date TEXT, journey_time TEXT,
FOREIGN KEY (travel_id) REFERENCES travels(id))
"""
cursor.execute(create_journey_table)

create_reservations_table = """
CREATE TABLE IF NOT EXISTS
Reservations(id INTEGER PRIMARY KEY, username TEXT,
journey_id INTEGER, row INTEGER, col INTEGER,
FOREIGN KEY (journey_id) REFERENCES Journey(id))
"""
cursor.execute(create_reservations_table)
db.commit()

# Insert travels
travels = [
    ('Washington-New York ', 7),
    ('London-Budapest', 8),
    ('Dubai-Mumbai', 7),
    ('Chennai-Delhi', 8),
    ('Sydney-Rio De Jeneiro', 7),
    ('Beijing-Moscow', 7),
    ('Amsterdam-Seoul', 8),
    ('Tokyo-Jakatra', 8),
    ('Abu Dhabi-Bughdad', 8),
    ('San Francisco-Singapore', 7),
    ('Kuala Lumpur-Mexico City', 7),
    ('Islamabad-Dhaka', 8),
    ('Auckland-Cyprus', 8),
    ('Prague-Rome', 6)
]


cursor.executemany(""" INSERT INTO travels(
travel_name, travel_rating) VALUES(?,?)
""", travels)
db.commit()

# Insert journeys
journeys = [
    (1, 'Emirates','2018-10-12', '09:00'),
    (1, 'Qatar travels', '2018-10-12', '10:00'),
    (2, 'Singapore travels', '2018-10-12', '08:00'),
    (2, 'Cathay Pacific travels', '2018-10-12', '12:00'),
    (3, 'ANA All Nippon travels', '2018-10-12', '09:00'),
    (4, 'Etihad', '2018-10-12','19:00'),
    (5, 'Turkish travels', '2018-10-12', '21:00'),
    (6, 'Qanatas travels', '2018-10-01', '22:00'),
    (6, 'Lufthansa', '2018-10-12', '10:00'),
    (7, 'Thai travels', '2018-10-12', '08:00'),
    (8, 'travel France', '2018-10-12', '12:00'),
    (8, 'Asiana travels', '2018-10-12', '0900'),
    (9, 'Austrian travels', '2018-10-12', '19:00'),
    (10, 'Austrian travels', '2018-10-12', '21:00'),
    (11, 'Emirates', '2018-10-12', '22:00'),
    (12, 'Etihad', '2018-10-12', '10:00'),
    (13, 'Qatar travels', '2018-10-12', '08:00'),
    (13, 'Emirates', '2018-10-12', '12:00'),
    (14, 'Etihad', '2018-10-12', '09:00'),
    (14, 'Qatar travels', '2018-10-12', '19:00')

]
cursor.executemany(""" INSERT INTO Journey(
travel_id, tour_name, journey_date, journey_time) VALUES(?,?,?,?)
""", journeys)
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
username, journey_id, row, col) VALUES(?,?,?,?)
""", reservations)
db.commit()