import pymysql

# establish the database connection
connection = pymysql.connect(
	host='localhost',
	user='root',
	password='',
	database='mytraining',
	cursorclass=pymysql.cursors.DictCursor
)

with connection:
	with connection.cursor() as cursor:
		# execute MySQL query using execute() method along with the cursor object
		cursor.execute("SELECT VERSION()")

		# fetchone() method or fetchall()[0] is used to fetch the single row.
		version = cursor.fetchone()
		print("Database version : %s" %version)
