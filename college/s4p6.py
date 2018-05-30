# WAP to help weatherman who will predict weather for a particualr week and for next seven days.
# Implement this scenario by creating two modules namely daily.py and weekly.py for predicting
# daily and weekly weather respectively.

from college.s4p6weekly import weeklyForcast
from college.s4p6daily import dailyForcast

weeklyForcast(int(input("Week number: ")))
dailyForcast(str(input("Day name:")))