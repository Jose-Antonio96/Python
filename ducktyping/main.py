# duck typing = concept where the class of an object is less important 
# than the methods/attributes
# class type is not checked fi minimum methods/attributes are present
# "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")
    
    def talk(self):
        print("The chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

person.catch(chicken)

# Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.