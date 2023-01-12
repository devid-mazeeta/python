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
		insert_query = """INSERT INTO student_details 
			(Reg_No, First_Name, Last_Name, Age, Sex, Department, Percentage)
			VALUES ('4','Arun','Kumar','24','M','BE','73.0')"""

		try:
			cursor.execute(insert_query) # executes table creation query
			connection.commit()	# commit or save the changes
		except Exception as e:
			print ("Error :: " + str(e))
			connection.rollback() # rollbacks the activity
