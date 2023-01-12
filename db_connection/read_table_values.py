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
		select_query = """SELECT * FROM student_details"""

		try:
			cursor.execute(select_query) # executes table creation query
			rows = cursor.fetchall() # returns all the row values
			# print(rows)

			for row in rows:
				reg_no = row["Reg_No"]
				f_name = row["First_Name"]
				l_name = row["Last_Name"]
				age = row["Age"]
				sex = row["Sex"]
				dept = row["Department"]
				percent = row["Percentage"]
				print ("Reg No :: %d , First Name :: %s , Last Name :: %s , Age :: %d , Sex :: %c , Department :: %s , Percentage :: %f" % (reg_no,f_name,l_name,age,sex,dept,percent))
		except Exception as e:
			print ("Error :: " + str(e))

### Output Structure ###

# [
#     {
#         "Reg_No":1,
#         "First_Name":"Devid",
#         "Last_Name":"Mazeeta",
#         "Age":28,
#         "Sex":"M",
#         "Department":"MBA",
#         "Percentage":70.0
#     },
#     {
#         "Reg_No":3,
#         "First_Name":"Arun",
#         "Last_Name":"Kumar",
#         "Age":24,
#         "Sex":"M",
#         "Department":"BE",
#         "Percentage":73.0
#     }
# ]