# Create class namely Employee. And show the Employee name, salary and count using OOP concept.

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayEmployee(self):
        print("Name:", self.name, "\nSalary:", self.salary)

emp1 = Employee("PREM", 1000)
emp2 = Employee("SHIVANG", 1500)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total:", Employee.empCount)