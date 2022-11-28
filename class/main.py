from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_1 = Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

#car.wheels = 2
Car.wheels = 2

car_1.drive()
car_1.stop()

print(car_1.wheels)