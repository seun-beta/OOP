class Fish:
    
    def __init__(self, first_name, last_name='Fish', skeleton='bone', eyelids=False):
        print("The object has been instantiated")
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")        


class Trout(Fish):
    pass


terry = Trout('Terry')
print(terry.skeleton)
print(terry.eyelids)
print(terry.last_name)
terry.swim()
terry.swim_backwards()


class Clownfish(Fish):

    def live_with_anemone(self):
        print("The clownfish coexists with sea anemone")


casey = Clownfish('Casey')
casey.live_with_anemone()
print(casey.eyelids)
print(casey.first_name)
