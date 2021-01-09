#class
class Employee:
    increment = 2 #class variable
    no_of_employee = 0
    #constructor
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.email = self.fname + self.lname + '@gmail.com'
        # self.increment = 1.4    #instance variable
        Employee.no_of_employee += 1

    @property
    def email(self):
        if self.fname==None:
            return 'Email Not set'
        else:
            return self.fname + '.' + self.lname + '@gmail.com'

    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        print(name_list)
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

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

if __name__ == "__main__":
    
    #object
    shadab = Employee('shadab', 'akhtar', 20000)
    dilshad = Employee('dilshad', 'ansari', 25000)
    dilshad.lname = 'akhtar'
    print(dilshad.email)

    dilshad.email = 'akhtar.dilshad@gmail.com'
    print(dilshad.email)
    del dilshad.email
    print(dilshad.email)