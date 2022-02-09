# Class created using class name
class Computer:
    # Its a method for class
    def config(self):
        print("i5, 8gb ram, 1tb HDD")

# TODO: Object Creation
# create comp1 object here and Computer() is a constructor
comp1 = Computer()
# create another object
comp2 = Computer()

# TODO: Call Method
# Its a simple way to understand the logic
Computer.config(comp1)
Computer.config(comp2)

# But in general we write like this
comp1.config()
comp2.config()
# TODO: We get same output after run this code.