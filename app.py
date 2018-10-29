from flask import Flask, render_template, jsonify, request
from Movie import Movie
from flight_project import Flight
from train import Train
import sqlite3


isloggedin = False
loggedinUsername=''

movie = Movie()
flight = Flight()
train = Train()

app = Flask(__name__)


@app.route("/")
def renderHome():
	return render_template("home.htm")

@app.route("/movie")
def renderMovie():
	movies = movie.getMovies()
	print(movies)
	return render_template("movie.htm", movies = movies)

@app.route("/movie/getShowTimes/<id>")
def sendShowTimes(id):
	showtimes = movie.getShowTimes(id)
	print(showtimes)
	return jsonify(showtimes=showtimes)

@app.route("/movie/book/<movie_id>/<projection_id>")
def bookMovie(movie_id, projection_id):
	current_movie = movie.getMovieById(movie_id)
	showtime = movie.getMovieShowtime(movie_id, projection_id)
	return render_template("bookMovie.htm", movie=current_movie[0], showtime=showtime[0])

@app.route("/flight")
def renderFlight():
	flights = flight.get_flights()
	print(flights)
	return render_template("flight.htm", flights=flights)

@app.route("/flight/<id>")
def sendFlights():
	return "NO Flights YET"

@app.route("/railway")
def renderRailway():
	trains = train.getTrain()
	return render_template("railway.htm", trains=trains)

@app.route("/railway/<id>")
def returnTrain(id):
	details=train.getRideTimes(id)
	return jsonify(details=details)

@app.route("/login")
def renderLogin():
	return render_template("login.htm")

@app.route("/login", methods=["POST"])
def authentication():
	global isloggedin, loggedinUsername
	ausername = request.form['username']
	apswrd = request.form['password']
	db = sqlite3.connect('movie_data.db')
	
	data = db.execute('''SELECT PASSWORD FROM LOGIN WHERE USERNAME = ?''',(ausername , ))
	if len(data)<=0:
		return "Error: Username doesnt exist"
	for row in data:
				if (row[0]==apswrd):
						isloggedin = True
						loggedinUsername = ausername
						return "User Logged in!"
	db.close()
	return "Error: Password Wrong!"

@app.route("/logout")
def logout():
	global isloggedin, loggedinUsername
	isloggedin=False
	loggedinUsername=False

@app.route("/register")
def renderRegister():
	return render_template("register.htm")

@app.route("/register", methods=["POST"])
def registeruser():
	db = sqlite3.connect('movie_data.db')
	db.execute('''CREATE TABLE IF NOT EXISTS LOGIN
				(USERNAME VARCHAR(50) PRIMARY KEY NOT NULL,
				NAME VARCHAR(50) NOT NULL,
				PHONE VARCHAR (15) NOT NULL,
				EMAILADDRESS VARCHAR(50) NOT NULL,
				PASSWORD VARCHAR (50) NOT NULL);''')
	username=request.form['username']
	pwrd=request.form['password']
	name=''
	phone=''
	eaddr=''
	print(username,name,phone,eaddr,pwrd)
	
	db.execute('''INSERT INTO LOGIN VALUES (?,?,?,?,?)''',(username,name,phone,eaddr,pwrd))
	db.commit()
	db.close()
	return "Success"

@app.route("/bus")
def renderBus():
	return render_template("bus.htm")

app.run(port=80, debug=True)

movie.close()
train.close()
flight.close()