import time
import calendar

# timestamp
timestamp = time.time()
print (timestamp)

# current time - returns in tuple
local_time = time.localtime()
print (local_time)

# current time - returns in tuple
cur_time = time.localtime(time.time())
print(cur_time)

# Getting formatted time
formatted_time1 = time.asctime(local_time)
print(formatted_time1)
formatted_time2 = time.asctime(cur_time)
print(formatted_time2)

# getting calendar for a month
cal = calendar.month(2018, 2)
print(cal)
