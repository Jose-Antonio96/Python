capitals = {"USA":"New York", "India":"New Dehli", "China":"Beijing", "Russia": "Kiev"}

capitals.update({"Germany":"Berlin"})
#update sirve tanto para añadir como cambiar valores ya existentes
capitals.pop("China") #esto remueve el key value pair
capitals.clear()#limpia todo el diccionario

print(capitals["Russia"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key, value)