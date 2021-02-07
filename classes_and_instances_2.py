class Employee():
    
    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.fname + ' ' + self.lname

def main():
    '''
    The following 'emp_1' and 'emp_2'
    are instances of the class Employee
    instance of a class, object, class instance, class object
    '''  

    emp_1 = Employee('Corey', 'Schafer', 1000)  
    emp_2 = Employee('Test', 'User', 2000)

    print(emp_1.fullname())
    Employee.fullname(emp_1)

if __name__ == '__main__':
    main()
