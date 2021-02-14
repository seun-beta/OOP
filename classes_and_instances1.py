class Employee():
    pass


emp_1 = Employee() 
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.pay = 1000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.pay = 2000

print(emp_1.pay)
print(emp_2.pay)
