import sqlite3
from prettytable import PrettyTable
from simple_settings import settings


# db = sqlite3.connect('travel_data.db')


# db.execute('''CREATE TABLE travels
#          (ID INT PRIMARY KEY  NOT NULL,
#          travel_name TEXT NOT NULL,
#          travel_rating INT NOT NULL);''')
#
# db.execute('''CREATE TABLE Journey
#          (ID INT PRIMARY KEY NOT NULL,
#          travel_id INT REFERENCES travels(id),
#          PROJECTIONS_TYPE TEXT NOT NULL,
#          PROJECTIONS_DATE  DATE NOT NULL,
#          journey_time TEXT NOT NULL );''')
#
# db.execute('''CREATE TABLE reservations
#          (ID INT PRIMARY KEY NOT NULL,
#          USERNAME TEXT NOT NULL,
#          journey_id INT REFERENCES Journey(ID),
#          ROW  INT NOT NULL,
#          COLUMN INT NOT NULL );''')



# db.execute('''INSERT INTO travels VALUES (1, 'Venom', 7)''')
# db.execute('''INSERT INTO travels VALUES (2, 'Iron Man', 8)''')
# db.execute('''INSERT INTO travels  VALUES (3, 'Spider-Man', 7)''')
# db.execute('''INSERT INTO travels VALUES (4, 'Black panther', 8)''')
# db.execute('''INSERT INTO travels VALUES (5, 'Harry potter and the chamber of secrets', 7)''')
# db.execute('''INSERT INTO travels VALUES (6, 'Greatest showman', 7)''')
# db.execute('''INSERT INTO travels  VALUES (7, 'La la land', 8)''')
# db.execute('''INSERT INTO travels VALUES (8, 'Titanic', 8)''')
# db.execute('''INSERT INTO travels VALUES (9, 'The Avengers', 8)''')
# db.execute('''INSERT INTO travels VALUES (10, 'Avengers age of ultron', 7)''')
# db.execute('''INSERT INTO travels VALUES (11, 'Thor', 7)''')
# db.execute('''INSERT INTO travels VALUES (12, 'Batman Arkham knight', 8)''')
# db.execute('''INSERT INTO travels VALUES (13, 'Flash', 8)''')
# db.execute('''INSERT INTO travels VALUES (14, 'Justice League', 6)''')
# db.commit()





# db.execute('''INSERT INTO Journey VALUES (1, 1, '3d','2018-10-12', '0900')''')
# db.execute('''INSERT INTO Journey VALUES (2, 1, '2d', '2018-10-12', '1000')''')
# db.execute('''INSERT INTO Journey VALUES (3, 2, '3d', '2018-10-12', '0800')''')
# db.execute('''INSERT INTO Journey VALUES (4, 2, '2d', '2018-10-12', '1200')''')
# db.execute('''INSERT INTO Journey VALUES (5, 3, '3d', '2018-10-12', '0900')''')
# db.execute('''INSERT INTO Journey VALUES (6, 4, '2d', '2018-10-12','1900')''')
# db.execute('''INSERT INTO Journey VALUES (7, 5, '3d', '2018-10-12', '2100')''')
# db.execute('''INSERT INTO Journey VALUES (8, 6, '2d', '2018-10-01', '2200')''')
# db.execute('''INSERT INTO Journey VALUES (9, 6, '3d', '2018-10-12', '1000')''')
# db.execute('''INSERT INTO Journey VALUES (10, 7, '2d', '2018-10-12', '0800')''')
# db.execute('''INSERT INTO Journey VALUES (11, 8, '2d', '2018-10-12', '1200')''')
# db.execute('''INSERT INTO Journey VALUES (12, 8, '3d', '2018-10-12', '0900')''')
# db.execute('''INSERT INTO Journey VALUES (13, 9, '3d', '2018-10-12', '1900')''')
# db.execute('''INSERT INTO Journey VALUES (14, 10, '2d', '2018-10-12', '2100')''')
# db.execute('''INSERT INTO Journey VALUES (15, 11, '3d', '2018-10-12', '2200')''')
# db.execute('''INSERT INTO Journey VALUES (16, 12, '2d', '2018-10-12', '1000')''')
# db.execute('''INSERT INTO Journey VALUES (17, 13, '2d', '2018-10-12', '0800')''')
# db.execute('''INSERT INTO Journey VALUES (18, 13, '3d', '2018-10-12', '1200')''')
# db.execute('''INSERT INTO Journey VALUES (19, 14, '3d', '2018-10-12', '0900')''')
# db.execute('''INSERT INTO Journey VALUES (20, 14, '3d', '2018-10-12', '1900')''')


# db.commit()

# cursor = db.execute("select * from reservations")
# for row in cursor:
#     print("id = ", row[0])
#     print("username= ", row[1])
#     print("proj_id = ", row[0])
#     print("row = ", row[1])
#     print("col = ", row[2], "\n")
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (9, 6, '3d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '1000')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (10, 7, '2d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '0800')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (11, 8, '2d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '1200')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (12, 8, '3d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '0900')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (13, 9, '3d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '1900')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (14, 10, '2d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '2100')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (15, 11, '3d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '2200')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (16, 12, '2d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '1000')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (17, 13, '2d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '0800')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (18, 13, '3d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '1200')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (19, 14, '3d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '0900')
# INSERT INTO "SYSTEM"."Journey" ("ID", "travel_id", "TYPE", "travelDATE", "TIME") VALUES (20, 14, '3d', TO_DATE('2018-10-12 06:20:13', 'YYYY-MM-DD HH24:MI:SS'), '1900')

# db.close()


class DBCommunicator:

    def __init__(self, cursor,db):
        self.cursor = cursor
        self.db = db
    def get_travels(self):
        return self.cursor.execute('''SELECT id, travel_name, travel_rating
                                        FROM travels
                                        ORDER BY travel_rating DESC''')

    def get_projections(self, travel_id):
        return self.cursor.execute('''SELECT Journey.id, tour_name, journey_time,
                                         journey_date, travel_id, travel_name
                                    FROM Journey
                                    JOIN travels
                                    ON Journey.travel_id = travels.id
                                    WHERE travel_id = ?
                                    ORDER BY journey_date''', (str(travel_id),))

    def get_projections_with_date(self, travel_id, date):
        return self.cursor.execute('''SELECT Journey.id, tour_name, journey_time,
                                             journey_date, travel_id, travel_name
                                      FROM Journey
                                      JOIN travels
                                      ON Journey.travel_id = travels.id
                                      WHERE travel_id = ? AND journey_date = ?
                                      ORDER BY journey_date''', (str(travel_id), str(date)))

    def get_revervations_for_projection(self, journey_id):
        return self.cursor.execute('''SELECT row, col
                                          FROM Reservations 
                                          WHERE journey_id = ?''', (journey_id,))

    def final_reservation(self, user, proj_id, row, col):
        self.cursor.execute('''INSERT INTO Reservations(
                                  username, journey_id, row, col) VALUES(?,?,?,?)''', (user, proj_id, row, col))
        self.db.commit()


class Controller:

    def __init__(self, db_communicator):
        self.db_communicator = db_communicator

    def generate_travels_table(self):
        table = PrettyTable(["id", "travel_name", "travel_rating"])
        for row in self.db_communicator.get_travels():
            table.add_row([row["id"], row["travel_name"], row["travel_rating"]])

        return table

    def create_cinema(self, journey_id):
        rows = 10
        cols = 10
        db_data = self.db_communicator.get_revervations_for_projection(journey_id)
        cinema = []

        row_headers = [" " if x == 0 else x for x in range(rows + 1)]
        cinema.append(row_headers)

        for row in range(rows):
            cinema.append([str(row + 1) if col == 0 else "." for col in range(cols + 1)])

        for row in db_data:
            cinema[row["row"]][row["col"]] = "X"

        return cinema

    def generate_journey_table(self, travel_id, date):
        if date is not None:
            db_result = self.db_communicator.get_projections_with_date(travel_id, date)
        else:
            db_result = self.db_communicator.get_projections(travel_id)

        table = PrettyTable(["journey_id", "tour_name", "journey_time",
                             "journey_date", "travel_id", "travel_name"])

        for row in db_result:
            table.add_row([row["id"], row["tour_name"], row["journey_time"],
                           row["journey_date"], row["travel_id"],
                           row["travel_name"]])

        return table

    def generate_reservations_table(self, data):
        table = PrettyTable(data[0])
        for row in data[1:]:
            table.add_row(row)

        return table

    def fin_reservation(self, user, journey_id, row, col):
        self.db_communicator.final_reservation(user,journey_id, row, col)


class CLI:

    def __init__(self, controller):
        self.controller = controller

        self.__user_is_active = True
        self.commands = {
            "show_travels": self.show_travels,
            "show_tours": self.show_tours,
            "make_reservations": self.make_reservations,
            "exit": self.exit
        }

    def show_travels(self, *args):
        print(self.controller.generate_travels_table())

    def show_tours(self, *args):
        travel_id = args[0]
        date = None
        if len(args) > 1:
            date = args[1]
        print(self.controller.generate_journey_table(travel_id, date))

    def show_reservations(self, data):
        print(self.controller.generate_reservations_table(data))

    def make_reservations(self, *args):
        username = input("Enter your name: ")
        number_of_tickets = int(input("Enter number of tickets: "))
        self.show_travels()
        travel_id = int(input("Enter travel id: "))
        self.show_tours(travel_id)
        journey_id = int(input("Enter journey id: "))
        self.show_reservations(self.controller.create_cinema(journey_id))
        # ask for ticket seats

        for i in range(number_of_tickets):
            ticketR = int(input("Enter Row: "))
            ticketC = int(input("Enter Column: "))
            self.controller.fin_reservation(username, journey_id, ticketR, ticketC)
            print("The ticket is booked\n")
        # if finalize
        # insert query

    def exit(self, *args):
        self.__user_is_active = False

    def start(self):
        print("Hello!")
        while self.__user_is_active:
            command = ""
            parameter1 = None
            parameter2 = None

            user_input = input("Enter command: ")
            user_input = user_input.split()
            command = user_input[0]
            if len(user_input) > 1:
                parameter1 = user_input[1]
                if len(user_input) > 2:
                    parameter2 = user_input[2]

            self.commands[command](parameter1, parameter2)


class Validator:
    def __init__(self):
        pass

    def validate_ticket(self):
        raise Exception("DA")


def main():
    db = sqlite3.connect("travel_db.db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    db_communicator = DBCommunicator(cursor,db)
    controller = Controller(db_communicator)
    cli = CLI(controller)
    cli.start()


if __name__ == '__main__':
    main()