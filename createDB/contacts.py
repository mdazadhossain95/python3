import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "1234", "python")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# # Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# # Create table as per requirement
# sql = """CREATE TABLE EMPLOYEE (
#    FIRST_NAME  CHAR(20) NOT NULL,
#    LAST_NAME  CHAR(20),1
#    AGE INT,
#    SEX CHAR(1),
#    INCOME FLOAT )"""

#INSERT
# Prepare SQL query to INSERT a record into the database.
# sql = """INSERT INTO contacts(name,
#    phone, email)
#    VALUES ('Azad', 01626364610,'mdazadhossain95@gmail.com')"""

# Prepare SQL query to UPDATE required records
# sql = "UPDATE contacts SET phone = 01626364610 WHERE name = 'Azad' "

# # Prepare SQL query to INSERT a record into the database.
# cursor.execute("SELECT * FROM contacts ")
#
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
#
# for name, phone, email in cursor:
#     print(name)
#     print(phone)
#     print(email)
#     print("-" * 20)
#
# cursor.close()
# db.commit()
# db.close()

# try:
#    # Execute the SQL command
#    cursor.execute(sql)
#    # Commit your changes in the database
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()

# disconnect from server
# db.close()

# Prepare SQL query to DELETE required records
sql = "DELETE FROM contacts WHERE name='Tim' "
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