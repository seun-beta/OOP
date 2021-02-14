class Employee():
    
    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.fname + ' ' + self.lname


def main():
    emp_1 = Employee('Corey', 'Schafer', 1000)  
    emp_2 = Employee('Test', 'User', 2000)

    print(emp_1.fullname())
    print(Employee.fullname(emp_1))

if __name__ == '__main__':
    main()
