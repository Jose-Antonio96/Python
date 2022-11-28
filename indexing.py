#Da acceso al elemento de una secuencia(str, list, tuples)
name = "lance lancy"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[0:3].upper()
#Especificamos del índice 0 al 
last_name = name[4:].lower()
#Del índice 4 hasta el final
last_character = name[-1]
#imprime el último elemento en una secuencia

print(first_name)
print(last_name)
print(last_character)