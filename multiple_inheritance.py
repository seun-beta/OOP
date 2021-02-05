class MobilePhone:

    def __init__(self, sim_slot_number, memory, ram):
        self.sim_slot_number = sim_slot_number
        self.memory = memory
        self.ram = ram
        
    def short_detail(self):
        result = 'Sim Slot Number:' + str(self.sim_slot_number) + ' RAM:' + str(self.ram) + ' Memory:' + str(self.memory)

        return result
                
        
class PhoneBrand:
    
    def brand(self,brand):
        return 'The brand of the phone is ' + brand  


class OperatingSystem(MobilePhone, PhoneBrand):
    pass


def main():
    os_1 = OperatingSystem(2,512,6)
    print(os_1.memory)
    print(os_1.ram)
    print(os_1.short_detail())
    print(os_1.brand('Samsung'))

    os_2 = OperatingSystem(1,64,2)
    print(os_2.memory)
    print(os_2.ram)
    print(os_2.short_detail())
    print(os_2.brand('Apple'))

if __name__ == '__main__':
    main()