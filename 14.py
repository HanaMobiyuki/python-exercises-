# Write a Python program to calculate number of days between two dates.
import datetime
first_date = datetime.date(2021,9,8)
last_date = datetime.date(2021,9,18)
diff = last_date - first_date
print(diff.days)