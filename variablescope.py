name = "Bro"
#A global and locally scoped versions of a variable can be created
def display_name():
    name = "Code" #local scope, available only inside this function
    print(name)

display_name()
print(name)

#Primero usa la versión local dentro de la función si está disponible, luego enclosed, luego global, y luego built-in
