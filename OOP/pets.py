class Pet():
    def __init__(self, name, breed, weight, height):
        self.name = name
        self.breed = None or breed
        self.weight = weight
        self.height = height
        self.hunger = 1
        self.sound = None

    def feed(self):
        # feed from can
        self.hunger = 1
        print("Open tin\nDump food into bowl\nGive bowl to pet")
        return


class Dog(Pet):
    def __init__(self, name, breed, weight, height):
        super().__init__(name, breed, weight, height)
        self.sound = "Bark"

    def walk(self):
        print("Grab leash\nWalk 45 mins")
        return
    
class Cat(Pet):
    def __init__(self, name, breed, weight, height):
        super().__init__(name, breed, weight, height)
        self.sound = "Meow"

class Rabbit(Pet):
    def __init__(self, name, breed, weight, height):
        super().__init__(name, breed, weight, height)
        self.sound = None
    
    def feed(self):
        print("Grab greens from fridge\nGrab kibble\nSet food in enclosure")
        return