#list = used to store multiple elements in a single variable

food = ["pizza", "hamburger", "hotdog", "pudding"]

food[0] = "sushi"

food.append("ice cream") #añade un elemento a la lista
food.remove("hotdog")
food.pop() #esto remueve el último elemento
food.insert(0, "cake") #en el index 0 ahora tenemos cake
food.sort() #ordena por vocabulario
food.clear() #borra todo en la lista
for x in food:
    print(x)


#2d lists = a lists of lists

drinks = []
dinner = []

food = [drinks, dinner]

print(food[0][1])

#tuple = like lists but are ordered and can't be changed
#used to group together data related

student = ("Lance", 26, "male")

print(student.count("Lance"))
print(student.index("male"))

for x in student:
    print(x)

if "Lance" in student:
    print("Lancy is here!")

#set = collection which is unordered, unindexed. No duplicates

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
dishes.update(utensils) #este une los sets
dinner_table = utensils.union(dishes) #este crea un set nuevo enteramente
print(utensils.differente(dishes)) #muestra las diferencias
print(utensils.intersection(dishes))
for x in dishes:
    print(x)


