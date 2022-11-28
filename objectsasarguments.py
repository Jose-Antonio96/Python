# objects as arguments

class Car:

    color = None

class Motorcycle:
    color = None

def change_color(vehicle,color):
    vehicle.color = color
#We can reuse this function for all kind of vehicles

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1, "red")
change_color(car_2, "brown")
change_color(car_3, "blue")
change_color(bike_1, "nigga")
#Basically, we pass a alue to a function. It can be a variable, value,
# or object passed to a function or method as input

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
