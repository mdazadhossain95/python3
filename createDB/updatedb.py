import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "1234", "python")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 5 WHERE SEX = '%c'" % 'M'
try:
	# Execute the SQL command
	cursor.execute(sql)
	# Commit your changes in the database
	db.commit()
except:
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()
