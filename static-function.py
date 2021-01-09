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

#use classmethod as alternative constructor
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day=="sunday":
            return False
        else:
            return True

#object
# shadab = Employee('shadab', 'akhtar', 20000)
# dilshad = Employee('dilshad', 'ansari', 25000)

shoaib = Employee.from_str("shoaib-ansari-30000")
print(Employee.isopen('sunday'))    #isopen is static method and it can be called by class or using object
print(shoaib.isopen('monday'))    #isopen is called using object

# print(shoaib.fname, shoaib.lname, shoaib.salary)