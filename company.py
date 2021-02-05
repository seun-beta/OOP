class Addax:
    office = 'Lagos Office'
    ext = '+234'
    num_of_emps = 0

    def __init__(self, first, last, age,sex, phone) :
        self.first = first
        self.last = last
        self.phone = phone 
        self.age = self.fullname()+ "'s age is: " + str(age)
        
       Addax.num_of_emps +=1  #For counting the number of employees added to the class.

        if sex == 'M':
            self.sex = 'Male'
        elif sex == 'F':
            self.sex = 'Female'
        else:
            self.sex = "Input a valid sex either 'M' or 'F'"
            
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def pnumber(self):
        self.pnumber = Addax.ext + str(self.phone)
        return self.pnumber
    def location(self):
        self.location = Addax.office
        return self.location
        
def main():
    addax_1 = Addax('Seun','Adegoke','21','M',812)
    print (addax_1.sex)
    print (addax_1.pnumber())
    print (addax_1.location())

    addax_2 = Addax('Jimoh','Muhammed',23,'M','867')
    print (addax_2.age)
    print (addax_1.age)

if __name__ == '__main__':
    main()

            
