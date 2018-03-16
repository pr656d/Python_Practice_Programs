# Rewrite compute salary program(s2p8) using try and except.

hours, rate = input("Hours: "), input("Rate: ")
try:
    if hours <= 40:
        salary = hours * rate
    else:
        salary = (40 * rate) + ((hours - 40) * (1.5 * rate))
except TypeError:
    hours, rate = float(hours), float(rate)
    if hours <= 40:
        salary = hours * rate
    else:
        salary = (40 * rate) + ((hours - 40) * (1.5 * rate))

    print("Salary:", salary)