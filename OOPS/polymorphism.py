# Polymorphism means “one thing, many forms.”
# In Object-Oriented Programming, it means:
# The same function or method can behave differently depending on the object using it.

                        # (or)
# One-line definition:-
# Polymorphism allows the same method name to behave differently in different classes.



class Animal:
    def sound(self):
        print("Sound")

class Dog(Animal):
    def sound(self):
        print("Bow... Bow...")

class Cat(Animal):
    def sound(self):
        print("Meow... Meow...")

a = Animal()

d = Dog()
d.sound()

c = Cat()
c.sound()