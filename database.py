import sqlite3


#query db and return all records
def show_all(table = 'reviews'):
	#connect
	conn = sqlite3.connect('customer.db') #creates db if it does not exist
	#create a cursor
	cur = conn.cursor() 
	
	#comes out as a tupple
	cur.execute("SELECT rowid, * from "+table)
	items = cur.fetchall();
	for item in items:
		print(item) #can be used with [] notation

	#do the execute
	conn.commit()

	#close the command
	conn.close()

#add a new record to the table
'''
reviews, name, location, comments
customers fname, lname, email
'''
def add_one(table, param1=' ', param2=' ', param3=' '):
	#connect
	conn = sqlite3.connect('customer.db') #creates db if it does not exist
	#create a cursor
	cur = conn.cursor() 
	
	#comes out as a tupple
	cur.execute("INSERT INTO "+ table +" VALUES (?,?,?)",(param1, param2, param3))

	#do the execute
	conn.commit()

	#close the command
	conn.close()

def delete_one(table = 'reviews', id = '0'):
	#connect
	conn = sqlite3.connect('customer.db') #creates db if it does not exist
	#create a cursor
	cur = conn.cursor() 
	
	#comes out as a tupple
	cur.execute("DELETE FROM "+ table +" WHERE rowid = (?)", id)

	#do the execute
	conn.commit()

	#close the command
	conn.close()

def email_lookup(email):
	#connect
	conn = sqlite3.connect('customer.db') #creates db if it does not exist
	#create a cursor
	cur = conn.cursor() 
	
	#comes out as a tupple
	cur.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,))

	items = cur.fetchall();
	for item in items:
		print(item) #can be used with [] notation
	#do the execute
	conn.commit()

	#close the command
	conn.close()