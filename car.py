# This program creates a subclass named Car_Model that inherits all the functionality of the class Car

    num_of_cars = 0

    def __init__(self, manufacturer, engine_capacity, seats, engine_type,fuel ):
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.seats = seats
        self.engine_type = engine_type
        Car.num_of_cars +=1 # counts the number of cars created

    def engine(self):
        return ('{} {} {} Engine'.format(self.engine_capacity,self.engine_type,self.fuel))

class Car_Model(Car):

    def __init__(self,manufacturer,  engine_capacity, seats, engine_type,fuel,model,year,edition,colour,custom_car):
        super().__init__(manufacturer, engine_capacity, seats, engine_type,fuel)
        self.model = model
        self.year = year
        self.edition = edition
        self.colour = colour
       
    
    def description(self):
        return 'Full description: {} {} {} {} {}'.format(self.manufacturer,self.model, self.year, self.edition,self.colour)
    
    def custom_car(self):
        if self.custom_car == 'Yes':
            print ('This car is a custom car')
        else :
            print ('This car is not a custom car')
            
# These are a few tests for the class Car

car_1 = Car('Toyota','4L','4','V6','Diesel')
car_model_1 = Car_Model('Toyota','4L','4','V6','Diesel','Camry','2020','SE','Blue','Yes')

print (car_model_1.description())
car_model_1.custom_car()

print (Car.num_of_cars)
 