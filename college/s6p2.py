# WAP to demonstrate usage of one try block with multiple except block and else clause
while True:
    try:
        n1, n2 = input("n1: "), input("n2: ")
        print("%d/%d = %f" % (float(n1), float(n2), float(n1) / float(n2)))
    except ZeroDivisionError:
        print("%d/%d: Can't divide by zero" % (float(n1), int(n2)))
    except NameError:
        print("Name exception")
    except TypeError:
        print("TypeError exception")
    except ValueError:
        print("ValueError exception")
    if input("PRESS y to exit: ") == 'y':
        break
