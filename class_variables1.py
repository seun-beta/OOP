class Employee:
    
    raise_amt = 1.05
    num_of_emps = 0

    def __init__(self, fname, lname, pay, language = 'English'):
        self.fname = fname 
        self.lname = lname
        self.pay = pay
        self.email = fname + ' '+ lname + '@email.com'
        self.language = language
        Employee.num_of_emps += 1

    def fullname(self):
        return self.fname + ' ' + self.lname   

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) 


emp_1 = Employee('Seun', 'Adegoke', 100)
emp_2 = Employee('Corey', 'Schafer', 200)

print(emp_1.pay)
Employee.raise_amt = 1.1
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.num_of_emps)
