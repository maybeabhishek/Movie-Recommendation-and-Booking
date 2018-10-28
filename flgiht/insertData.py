import sqlite3
db = sqlite3.connect("flight_db.db")
cursor = db.cursor()

# Create tables
create_flight_table = """
CREATE TABLE IF NOT EXISTS
Flights(id INTEGER PRIMARY KEY, flight_name TEXT, flight_rating FLOAT)
"""
cursor.execute(create_flight_table)

create_journey_table = """
CREATE TABLE IF NOT EXISTS
Journey(id INTEGER PRIMARY KEY, flight_id INTEGER, journey_type TEXT,
journey_date TEXT, journey_time TEXT,
FOREIGN KEY (flight_id) REFERENCES Flights(id))
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

# Insert Flights
flights = [
    ('Emirates', 7),
    ('Qatar Airways', 8),
    ('Singapore Airlines', 7),
    ('Cathay Pacific Airways', 8),
    ('ANA All Nippon Airways', 7),
    ('Etihad', 7),
    ('Turkish Airlines', 8),
    ('EVA Air', 8),
    ('Qanatas Airways', 8),
    ('Lufthansa', 7),
    ('Thai Airways', 7),
    ('Air France', 8),
    ('Asiana Airlines', 8),
    ('Austrian Airlines', 6)
]


cursor.executemany(""" INSERT INTO Flights(
flight_name, flight_rating) VALUES(?,?)
""", flights)
db.commit()

# Insert Projections
projections = [
    (1, 'Washington-New York,Business','2018-10-12', '09:00'),
    (1, 'London-Budapest,Economy', '2018-10-12', '10:00'),
    (2, 'Dubai-Mumbai,Business', '2018-10-12', '08:00'),
    (2, 'Chennai-Delhi,Economy', '2018-10-12', '12:00'),
    (3, 'Sydney-Rio De Jeneiro,Business', '2018-10-12', '09:00'),
    (4, 'Beijing-Moscow,Economy', '2018-10-12','19:00'),
    (5, 'Amsterdam-Seoul,Business', '2018-10-12', '21:00'),
    (6, 'Tokyo-Jakatra,Economy', '2018-10-01', '22:00'),
    (6, 'Abu Dhabi-Bughdad,Business', '2018-10-12', '10:00'),
    (7, 'San Francisco-Singapore,Economy', '2018-10-12', '08:00'),
    (8, 'Kuala Lumpur-Mexico City,Economy', '2018-10-12', '12:00'),
    (8, 'Islamabad-Dhaka,Business', '2018-10-12', '0900'),
    (9, 'Auckland-Cyprus,Business', '2018-10-12', '19:00'),
    (10, 'Prague-Rome,Economy', '2018-10-12', '21:00'),
    (11, 'Bangkok-Frankfurt,Business', '2018-10-12', '22:00'),
    (12, 'Munich-Hyderabad,Economy', '2018-10-12', '10:00'),
    (13, 'Madrid-las Vegas,Economy', '2018-10-12', '08:00'),
    (13, 'Athens-Milan,Business', '2018-10-12', '12:00'),
    (14, 'Toronto-Haiti,Business', '2018-10-12', '09:00'),
    (14, 'Delhi-Mumbai,Business', '2018-10-12', '19:00')

]
cursor.executemany(""" INSERT INTO Projections(
movie_id, journey_type, journey_date, journey_time) VALUES(?,?,?,?)
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
username, journey_id, row, col) VALUES(?,?,?,?)
""", reservations)
db.commit()