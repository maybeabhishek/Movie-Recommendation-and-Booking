import sqlite3

class Movie:
  def __init__(self):
    self.conn = sqlite3.connect("movie_db.db", check_same_thread=False)

  def getMovies(self):
    cur = self.conn.cursor()
    cur.execute("Select MOVIE_NAME, ID from MOVIES")
    rows = cur.fetchall()
    return rows
  
  def getShowTimes(self, movieId):
    cur = self.conn.cursor()
    cur.execute("Select movie_id, projection_type, projection_date, projection_time from Projections where movie_id="+movieId+" order by projection_date")
    rows = cur.fetchall()
    return rows
