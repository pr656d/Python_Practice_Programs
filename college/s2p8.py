# WAP to prompt the user for hours and rate per hour to compute gross pay.
# Company will give the employee 1.5 times the hourly rate for hours worked above 40 hours.


hours, rate = float(input("Hours: ")), float(input("Rate: "))
if hours <= 40:
    salary = hours * rate
else:
    salary = (40 * rate) + ((hours - 40) * (1.5 * rate))

print("Salary:", salary)
