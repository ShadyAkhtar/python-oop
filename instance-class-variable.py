#class
class Employee:
    increment = 1.5 #class variable
    no_of_employee = 0
    #constructor
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.4    #instance variable
        Employee.no_of_employee += 1

    def increase(self):
        # self.salary = int(self.salary * increment) # Wrong declaration, have to mention self or Employee
        self.salary = int(self.salary * self.increment)
        # self.salary = int(self.salary * Employee.increment) #Class variable

#object
shadab = Employee('shadab', 'akhtar', 20000)
dilshad = Employee('dilshad', 'ansari', 25000)

shadab.increase()

print("No. Of Employees : ", Employee.no_of_employee)

# print(shadab, dilshad)

print("Shadab-FirstName : " + shadab.fname, "Salary : " , shadab.salary, "\n", "Dilshad-FirstName : " + dilshad.fname, "Salary : " , dilshad.salary)

shadab.hey = 10 #this will declare new variable "hey" to object named "shadab"
print("Variables of shadab : ", shadab.__dict__) # it will display the all variable to shadab object

# Employee.he = 1 # cannot declare because Employee is a class and cannot be manipulated by outside like object
print("variables of Employee class : ", Employee.__dict__)