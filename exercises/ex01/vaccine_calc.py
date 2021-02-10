"""A vaccination calculator."""

__author__ = "730393936"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
# Begin your solution here...
from datetime import datetime, timedelta
today: datetime = datetime.today()
pop = int(input("Population:"))
dos_admin = int(input("Doses administered:"))
dos_per_day = int(input("Doses per day:"))
target_percent = int(input("Target percent vaccinated:"))
days = ((target_percent / 100) * pop - (dos_admin / 2)) / (dos_per_day / 2)
est_days: int = round(days)
print(str(est_days) + " days" )
vac_days: timedelta = timedelta(days)
future: datetime = today + vac_days
print(future.strftime("%B %d, %Y"))
print("We will reach " + str(target_percent) + "% vaccination in " + str(est_days) + " days ")
print("on " + future.strftime("%B %d, %Y"))