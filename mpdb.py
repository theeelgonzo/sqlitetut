import sqlite3

# establish connection to tutorial.db
# create tutorial.db if it does not exist
con = sqlite3.connect('tutorial.db')

#create cursor for db selection
cur = con.cursor()

# create table 'Movies' in tutorial db with execute method
# cur.execute('CREATE TABLE movie(title, year, score)')

# query db to ensure movie table exists
res = cur.execute('SELECT name FROM sqlite_master')
#print(res.fetchone())

res = cur.execute("SELECT name FROM sqlite_master WHERE name = 'spam'")
#print(res.fetchone() is None)
# print True because there is no spam -\_0_/-
# add records into movie table
#cur.execute(
 #       """
  #      INSERT INTO
   #     movie
    #    VALUES
     #   ('Monty Python And The Holy Grail', 1975, 8.2),
      #  ('And Now For Something Completely Different', 1971, 7.5)
       # """
       # )
res = cur.execute('SELECT * FROM movie')
#print(res.fetchall())
#con.commit()

res = cur.execute('SELECT score FROM movie')

#print(res.fetchall())
#data = [
#        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#        ("Monty Python's The Meaning of Life", 1983, 7.5),
#        ("Monty Python's The Life of Brian", 1979, 8.0)
#        ]
#cur.executemany("INSERT INTO movie VALUES (?, ?, ?)", data)
#con.commit()
res = cur.execute('SELECT * FROM movie')
#print(res.fetchall())
for row in cur.execute('SELECT year, title FROM movie ORDER BY year'):
    print(row)
con.close()
new_con = sqlite3.connect('tutorial.db')
new_cur = new_con.cursor()
res = new_cur.execute('SELECT title, year FROM movie ORDER BY score DESC')
title, year = res.fetchone()
print(f"The highest scoring Monty Python movie is {title!r}, released in {year}.")
