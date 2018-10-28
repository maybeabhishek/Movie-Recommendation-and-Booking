from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def renderHome():
  return render_template("home.htm")

@app.route("/movie")
def renderMovie():
  return render_template("movie.htm")

@app.route("/flight")
def renderFlight():
  return render_template("flight.htm")

app.run(port=80, debug=True)