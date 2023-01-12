import pymysql

# establish the database connection
connection = pymysql.connect(
	host='localhost',
	user='root',
	password='',
	database='mytraining',
	cursorclass=pymysql.cursors.DictCursor
)

# prepare a cursor object using database connection object and cursor() method
with connection:
	with connection.cursor() as cursor: 

		# defining table drop query
		drop_query = 'DROP TABLE IF EXISTS student_details'
		# executes table drop query
		cursor.execute(drop_query)

		# defining table creation query
		create_query = """CREATE TABLE student_details (
			Reg_No INT(12) NOT NULL PRIMARY KEY,
			First_Name  VARCHAR(30) NOT NULL,
			Last_Name  CHAR(30),
			Age INT(2) NOT NULL,
			Sex CHAR(1) NOT NULL,
			Department VARCHAR(20) NOT NULL,
			Percentage FLOAT(5) NOT NULL )"""

		# executes table creation query
		cursor.execute(create_query)
