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
		update_query = "UPDATE student_details SET Age = '28' WHERE Reg_No = '3'"

		try:
			cursor.execute(update_query) # executes table creation query
			connection.commit()	# commit or save the changes
		except Exception as e:
			print ("Error :: " + str(e))
			connection.rollback() # rollbacks the activity
