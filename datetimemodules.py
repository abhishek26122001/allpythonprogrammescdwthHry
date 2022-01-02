# date: its just manipulate date (Month, day, year)
# time : time independent of the day(Hour, minute, second, microsecond)
# datetime : (Month, day, year, hour, sec, microsecond)
#timedelta: A duration of time used for manipulating dates
#tzinfo: An abstract class for dealing with time zone

print("Getting todays date: ")

from datetime import date
from datetime import time
from datetime import datetime
today = date.today()
print("Date is: ",today)
print("Day: ",today.day)
print("Month: ",today.month)
print("Year: ",today.year)
print("Week-Day: ",today.weekday())

print("\n")

print("Current Date and time: ")

from datetime import date
from datetime import time
from datetime import datetime
today = datetime.now()
print("Current time and date: ",today)
print("Current Time: ",datetime.time(datetime.now()))

print("\n")

print("Week Days: ")
w = date.weekday(today)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Today is day:  %d" % w)
print("Which is a " + days[w])

print("\n")

print("Formatting Date and Time: ")

#%y/%Y: is used for Years
#%a/%A  : is used for Weekdays
#%b/%B: is used for Months
#%d : is used for day of months
# % C : is used to display local date and time
#%x: locals date
#%X: local's time
#%i/%H: 12/24Hr
#%M : Minnutes
#%S: SEconds
#%p: local's AM/PM

from datetime import date
from datetime import datetime
dt = datetime.now()

print(dt.strftime("%c"))
print(dt.strftime("%x"))
print(dt.strftime("%X"))
print(dt.strftime("%I:%M:%S %p"))
print(dt.strftime("%H: %M"))
print(dt.strftime("%y"))
print(dt.strftime("%b"))
print(dt.strftime("%a"))
print(dt.strftime("%A - %d - %B - %Y"))


print("\n")

print("Time delta object: ")

# This is used to estimate time for both future and past

from datetime import date, datetime, timedelta
today = datetime.now()
d =today - timedelta(days= 90)
print(d)