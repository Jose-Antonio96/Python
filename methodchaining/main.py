# Method chaining = calling multiple methods sequentally
# each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self
        
car = Car()

car.turn_on().drive()