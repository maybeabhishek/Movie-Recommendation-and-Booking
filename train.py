import sqlite3

class Train:
	def __init__(self):
		self.conn = sqlite3.connect("train_db.db", check_same_thread=False)

	def close(self):
		self.conn.close()

	def getTrain(self):
		cur = self.conn.cursor()
		cur.execute("SELECT id, train_name, train_rating FROM trains ORDER BY train_rating DESC")
		rows = cur.fetchall()
		return rows
	
	def getTrainById(self, trainId):
		cur = self.conn.cursor()
		cur.execute("Select train_name from trains where id="+trainId)
		rows = cur.fetchall()
		return rows

	def getRideTimes(self, trainId):
		cur = self.conn.cursor()
		cur.execute("Select train_id, journey_type, journey_date, journey_time, id from Journey where train_id="+trainId+" order by journey_date")
		rows = cur.fetchall()
		return rows

	def getJourneyRideTime(self, travelId, jId):
		cur = self.conn.cursor()
		cur.execute("Select train_id, journey_type, journey_date, journey_time, id from Journey where train_id="+travelId+" and id="+jId+" order by journey_date")
		rows = cur.fetchall()
		return rows
		
	# # def make_reservations(self, *args):
	# 	username = input("Enter your name: ")
	# 	number_of_tickets = int(input("Enter number of tickets: "))
	# 	train_id = int(input("Enter travel id: "))
	# 	journey_id = int(input("Enter journey id: "))
	# 	for i in range(number_of_tickets):
	# 		ticketR = int(input("Enter Row: "))
	# 		ticketC = int(input("Enter Column: "))
	# 		cur = self.conn.cursor()
	# 		cur.execute('''INSERT INTO Reservations(username, journey_id, row, col) VALUES(?,?,?,?)''', (username, train_id,ticketR,ticketC)))
	# 		self.db.commit()
	# 		print("The ticket is booked\n")