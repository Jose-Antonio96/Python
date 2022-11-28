#*args = parameter that will pack all arguemnts into a tuple

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[4] = 3
    for i in stuff:
        sum+= i
    return sum

print(add(1,2,3,4,5,6))