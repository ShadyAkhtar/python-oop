#class
class Employee:
    #constructor
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

#object
shadab = Employee('shadab', 'akhtar', 20000)
dilshad = Employee('dilshad', 'ansari', 25000)

print(shadab, dilshad)
print("Shadab-FirstName : " + shadab.fname, "Salary : " , shadab.salary, "\n", "Dilshad-FirstName : " + dilshad.fname, "Salary : " , dilshad.salary)

