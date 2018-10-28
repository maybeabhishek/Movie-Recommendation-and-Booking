from flask import Flask, render_template, jsonify
from Movie import Movie

movie = Movie()
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

@app.route("/flight")
def renderFlight():
  return render_template("flight.htm")

@app.route("/login")
def renderLogin():
  return render_template("login.htm")

@app.route("/register")
def renderRegister():
  return render_template("register.htm")
app.run(port=8081, debug=True)