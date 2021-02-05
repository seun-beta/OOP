class ComplexNumber :

    num = 0
    
    def __init__(self, real, imaginary):
        self.real = real 
        self.imaginary = imaginary
        ComplexNumber.num +=1 #for counting the number of times the class was instantiated

    def normal (self):
        a =self.real
        b = ' + sqrt'+str((-1*self.imaginary**2))
        return a,b

    def stylize(self):
        return self.real, (str(self.imaginary)+ 'i')

    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return real_part,imaginary_part

    def __repr__(self):
        return "ComplexNumber({},{})".format(self.real,self.imaginary)

    def __str__ (self):
        return '{} is the real part while {} is the imaginary part'.format(self.real, self.imaginary)

# Testing the code  

complex_1 = ComplexNumber(2,5)
complex_2 = ComplexNumber(13,67)
complex_3 = ComplexNumber(345,87)

print (complex_1.__repr__())
print (repr(complex_1))
print()
print (complex_1.__str__())
print (str(complex_1))
print()
print (complex_1.__add__(complex_3))
print(complex_1+complex_3)
print (complex_1.stylize())

print (ComplexNumber.num)
print (complex_1.normal())

