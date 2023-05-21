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

