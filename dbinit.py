import sqlite3

# connect(s)/creates
conn = sqlite3.connect('travelsite.db') #creates db if it does not exist

# create a cursor
cur = conn.cursor()

# create a table with a doc string sqlite is case sensitive
#u sing """ lets us put this on multiple lines. Single quotes has to be in one line
# Sqlite use the following data types: NULL, INTEGER (WHOLE NUMBER), REAL (DECIMAL VALUES), TEXT (STRING), BLOB (code)

# cur.execute("""CREATE TABLE reviews (
# 		name text,
# 		location text,
# 		comments text
# 	)""")

# cur.execute("INSERT INTO reviews VALUES ('Joe', 'Central Park', 'It was so nice!')")
# cur.execute("INSERT INTO reviews VALUES ('Mitch', 'Empire State Building', 'It was so tall!')")
# comes out as a tupple
cur.execute("SELECT rowid, * from reviews")
items = cur.fetchall();


for item in items:
	print(item[0], item[1], item[2], item[3])
# can be used with [] notation



#do the execute
conn.commit()

#close the command
conn.close()
