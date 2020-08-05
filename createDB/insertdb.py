import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "1234", "python")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
  		 LAST_NAME, AGE, SEX, INCOME)
  		 VALUES ('Azad', 'Hossain', 22, 'M', 1999)"""
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