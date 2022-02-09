# TODO: Before Without __init__
class Computer2:
    def specs(self):
        return f"The brand is: {self.brand} and the processor is: {self.cpu2} last ram is:{self.ram2}"


c1 = Computer2()
c1.brand = "HP"
c1.cpu2 = "i3"
c1.ram2 = "4 GB"
# We return here we need to print it
print(c1.specs())

# TODO: The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach.
# The __init__ function is called every time an object is created from a class.
# The __init__ method lets the class initialize the object's attributes and serves no other purpose.
# It is only used within classes.


class Computer:
    # Its our init method with 2 parameter
    # __init__ its a special type of function

    def __init__(self, cpu, ram):
        # here we declare attribute/variable using same name
        # cpu=cpu
        self.cpu = cpu
        # here we declare attribute/variable using diff name
        # r = ram
        self.r = ram

    def config(self):
        # We need to add self before passing variable
        print("Object_n config is:", self.cpu, self.r)


# TODO: Object Creation with parameter as declare in __init__
comp1 = Computer("intel core i5", 8)
comp2 = Computer("AMD Ryzen 3", 16)

# TODO: Call the Object.method
comp1.config()
comp2.config()


