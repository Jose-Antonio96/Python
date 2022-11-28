
from multiprocessing.spawn import import_main_path


print("I love python")
print("I don't love php")
#variable = contenedor de un valor. Podemos añadir numeros, booleanos, palabras

#first_name = "Oberdrid"
#second_name = "Lancelot" 
#full_name= first_name +" "+ second_name
#print(type(first_name))
#print("Hello, I am "+name)
#print("Hello "+full_name)

age = 21
age += 1
#Esto es como un shortcut
#print(age)
print(type(age))
print("Your age is: "+str(age))
#El str convierte la variable a un string, y así podemos mostrarlo con otro string
#Un int no puede estar entre comillas

height = 250.5
#Esto es un float "floating point number"
print("your height is: "+str(height) + "cm")
print(type(height))

human = False
print(human)
print(type(human))
print("Are you a human: "+str(human))

#multiple assignments = multiples variable al mismo tiempo en una linea de codigo
#name = "Oberdrid"
#age = 21
#attractive = True
name, age, attractive = "Oberdrid", 21, True
print (name)
print (age)
print (attractive)

Spongebob = Patric = Sandy = Squidward = 30
print (Spongebob)
print (Sandy)
print (Patric)
print (Squidward)

#STRING METHODS 
name = "Oberdrid"
#print(len(name))
#print(name.find("d"))
#print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("i","a"))
print(name*3)

#TYPE CASTING
#Cambia el tipo de data de un valor a otro tipo de data
x = 1 #int
y = 2.0 #float
z = "3" #str

x = float(x)
y = int(y)
z = int(z)

print(x)
print(y)
print(z*3)
print("X is "+str(x))
print("Y is "+str(y))

#USER INPUT
name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age = age + 1

print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+" cm tall")

