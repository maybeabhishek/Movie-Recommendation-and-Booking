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

@app.route("/movie/book/<movie_id>/<projection_id>")
def bookMovie(movie_id, projection_id):
  current_movie = movie.getMovieById(movie_id)
  showtime = movie.getMovieShowtime(movie_id, projection_id)
  return render_template("bookMovie.htm", movie=current_movie[0], showtime=showtime[0])

@app.route("/flight")
def renderFlight():
  return render_template("flight.htm")

@app.route("/railway")
def renderRailway():
  return render_template("railway.htm")
@app.route("/login")
def renderLogin():
  return render_template("login.htm")

@app.route("/register")
def renderRegister():
  return render_template("register.htm")





app.run(port=80, debug=True)
movie.close()
