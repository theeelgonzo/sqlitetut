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
print(res.fetchone())

res = cur.execute("SELECT name FROM sqlite_master WHERE name = 'spam'")
print(res.fetchone() is None)
# print True because there is no spam -\_0_/-
# add records into movie table
cur.execute(
        """
        INSERT INTO
        movie
        VALUES
        ('Monty Python And The Holy Grail', 1975, 8.2),
        ('And Now For Something Completely Different', 1971, 7.5)
        """
        )
res = cur.execute('SELECT * FROM movie')
print(res.fetchall())
