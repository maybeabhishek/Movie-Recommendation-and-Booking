from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def renderHome():
  return render_template("home.htm")

@app.route("/movie")
def renderMove():
  return render_template("movie.htm")

app.run(port=80, debug=True)