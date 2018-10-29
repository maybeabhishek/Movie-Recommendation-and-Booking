import sqlite3

class Movie:
  def __init__(self):
    self.conn = sqlite3.connect("movie_db.db", check_same_thread=False)

  def close(self):
    self.conn.close()

  def getMovies(self):
    cur = self.conn.cursor()
    cur.execute("Select MOVIE_NAME, ID from MOVIES")
    rows = cur.fetchall()
    return rows
  
  def getMovieById(self, movieId):
    cur = self.conn.cursor()
    cur.execute("Select MOVIE_NAME from MOVIES where id="+movieId)
    rows = cur.fetchall()
    return rows

  def getShowTimes(self, movieId):
    cur = self.conn.cursor()
    cur.execute("Select movie_id, projection_type, projection_date, projection_time, id from Projections where movie_id="+movieId+" order by projection_date")
    rows = cur.fetchall()
    return rows

  def getMovieShowtime(self, movieId, projectionId):
    cur = self.conn.cursor()
    cur.execute("Select movie_id, projection_type, projection_date, projection_time, id from Projections where movie_id="+movieId+" and id="+projectionId+" order by projection_date")
    rows = cur.fetchall()
    return rows