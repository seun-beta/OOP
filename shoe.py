class Shoe:
    
    # Class variables 'brand' & 'group'
    brand = 'Nike'
    group = 'Men'

    # Instance variables 'name' & 'size' from the constructor method 
    def __init__(self, name, size):
        self.name = name
        self.size = size

    # Instance variable 'outsole' from the method 
    def outsole_material(self, outsole):
        return ("The outsole material is " + outsole)


def main():
    shoe_1 = Shoe('Air Max', 42)
    print(shoe_1.name)
    print(shoe_1.size)
    print(shoe_1.brand)
    shoe_1.outsole_material('Natural Rubber')
    print()
    shoe_2 = Shoe('React', 56)
    print(shoe_2.brand)
    print(shoe_2.name)
    print(shoe_2.size)
    shoe_2.outsole_material('Polyuretane')  

if __name__ =='__main__':
    main()
