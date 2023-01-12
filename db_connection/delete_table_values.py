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

		# defining table creation query
		delete_query = "DELETE FROM `student_details` WHERE Age = '24'"

		try:
			cursor.execute(delete_query) # executes table creation query
			connection.commit()	# commit or save the changes
		except Exception as e:
			print ("Error :: " + str(e))
			connection.rollback() # rollbacks the activity
