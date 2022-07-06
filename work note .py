from datetime import date

# calling the today
# function of date class
today = date.today()

print("Today's date is", today)

# Converting the date to the string
from datetime import date

# calling the today
# function of date class
today = date.today()

print("Today's date is", today)

# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))

a = 80
data = a - 90
p = data / a * 100
print(p)