#class
class Employee:
    increment = 1 #class variable
    no_of_employee = 0
    #constructor
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.increment = 1.4    #instance variable
        Employee.no_of_employee += 1

    def increase(self):
        # self.salary = int(self.salary * increment) # Wrong declaration, have to mention self or Employee
        self.salary = int(self.salary * self.increment)
        # self.salary = int(self.salary * Employee.increment) #Class variable

    @classmethod    #decorator
    def change_increment(cls,amount):
        cls.increment = amount

#object
shadab = Employee('shadab', 'akhtar', 20000)
dilshad = Employee('dilshad', 'ansari', 25000)

#Before
print(shadab.salary)

# Increment
Employee.change_increment(2)
shadab.increase()

#After Increment
print(shadab.salary)

